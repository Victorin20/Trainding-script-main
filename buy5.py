import MetaTrader5 as mt5

mt5.initialize()

startPrice = 1.04000
volume = 0.06
points = 0.0025

path = "C:/Users/Public/buy5.txt"

# Select the desired symbol
symbol = "EURUSD"

failed = False
succes = False
failures = 0

try:
    f = open(path, "r")
    failures = f.read()
    failures = int(failures)
    if(failures>=16):
        failures = 0
    f.close()
except:
    print("path not found")

def cancel_order(order_number):
    # Create the request
    request = {
        "action": mt5.TRADE_ACTION_REMOVE,
        "order": order_number,
        "comment": "Order Removed"
    }
    # Send order to MT5
    order_result = mt5.order_send(request)
    return order_result

def cancel_buyLimit_order():
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_LIMIT and order.state == mt5.ORDER_STATE_PLACED:
            order_to_remove = order
            break

    cancel_order(order_to_remove.ticket)

def cancel_SellLimit_order():
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_LIMIT and order.state == mt5.ORDER_STATE_PLACED:
            order_to_remove = order
            break

    cancel_order(order_to_remove.ticket)

def cancel_buyStop_order():
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_STOP and order.state == mt5.ORDER_STATE_PLACED:
            order_to_remove = order
            break

    cancel_order(order_to_remove.ticket)

def buyLimit(position, volume):
    symbol = "EURUSD"  # EUR/USD currency pair
    order_type = mt5.ORDER_TYPE_BUY_LIMIT       # Replace with the desired volume/lot size
    price = startPrice + position * points     # Set the price for the Buy Limit order
    stop_loss = price - points  # Replace with the desired stop loss price
    take_profit = price + points  # Replace with the desired take profit price
    request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": volume,
    "type": order_type,
    "price": price,
    "sl":stop_loss,
    "tp":take_profit,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Limit order placed successfully. Order ticket:", result.order)

def buyStop(position, volume):
    symbol = "EURUSD"  # EUR/USD currency pair
    order_type = mt5.ORDER_TYPE_BUY_STOP       # Replace with the desired volume/lot size
    price = startPrice + position * points     # Set the price for the Buy Limit order
    stop_loss = price - points  # Replace with the desired stop loss price
    take_profit = price + points  # Replace with the desired take profit price
    request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": volume,
    "type": order_type,
    "price": price,
    "sl":stop_loss,
    "tp":take_profit,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Stop order placed successfully. Order ticket:", result.order)

def sellLimit(position, volume):
    symbol = "EURUSD"  # Replace with the desired symbol
    order_type = mt5.ORDER_TYPE_SELL_LIMIT
    price = startPrice + position * points
    stop_loss = price + points  # Replace with the desired stop loss price
    take_profit = price - points  # Replace with the desired take profit price

    request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": volume,
    "type": order_type,
    "price": price,
    "sl": stop_loss,
    "tp": take_profit,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Order placement failed. Error code:", result.retcode)
    else:
        print("SellLimit order placed successfully. Order ticket:", result.order)
  
first_active = True
second_active = False
third_active = False
fourd_active = False
fifth_active = False
sixth_active = False

third = False
fourd = False
fifth = False
sixth = False


buyLimit(0, volume)
buyStop(1, volume*2)

while failed == False and succes == True:

    last_price = mt5.symbol_info_tick(symbol).ask
    
    if(first_active and last_price <= startPrice - points):
        failed = True
        cancel_buyStop_order()

    if(first_active and last_price >= startPrice + points):
        first_active = False
        second_active = True

    if(second_active and last_price <= startPrice):
        failed = True
        cancel_buyStop_order()

    if(second_active and last_price >= startPrice + points*2):
        second_active = False
        third_active = True

    if(third_active and last_price <= startPrice + points):       
        failed = True
        cancel_SellLimit_order()
    
    if(third_active and last_price >= startPrice + points*3):
        third_active = False    
        fourd_active = True
    
    if(fourd_active and last_price >= startPrice + points*4):
        failed = True
        cancel_buyLimit_order()

    if(fourd_active and last_price <= startPrice +points*2):
        fourd_active = False
        fifth_active = True
    
    if(fifth_active and last_price <= startPrice + points):
        failed = True
        cancel_buyStop_order()

    if(fifth_active and last_price >= startPrice + points*3):
        fifth_active = False
        sixth_active = True
    
    if(sixth_active and last_price <= startPrice + points*2):
        failed = True
    
    if(sixth_active and last_price >= startPrice + points*4):
        sixth_active = False
        succes = True

    if(failed == False):

        if(last_price >= startPrice + points and third == False and second_active):    
            buyStop(2, volume*4)
            third = True

        if(last_price >= startPrice + points * 2 and fourd == False and third_active):
            sellLimit(3, volume*8)
            fourd = True
        
        if(last_price >= startPrice + points * 3 and fifth == False and fourd_active):
            buyLimit(2, volume*16)
            fifth = True
        
        if(last_price <= startPrice + points * 2 and sixth == False and fifth_active):
            buyStop(3, volume*32)
            sixth = True
        

if(failed):
    failures+=1

if(succes):
    failures = 0

try:
    with open(path, 'w') as file:
        failures = str(failures)
        file.write(failures)
except:
    print("path not found")

if(succes):
    print("Succes you win ")
else : 
    print("Failed")
 
mt5.shutdown()