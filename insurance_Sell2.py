import MetaTrader5 as mt5

mt5.initialize()

startPrice = 1.08400
volume = 0.16
black_volume = 0.1
points = 0.0025

blackbuyStop_stopLoss = 75
blackbuyStop_takeProfit = 50
blackSellLimit_takeProfit = 75
blackSellLimit_stopLoss = 50
one_lot = 10


path = "C:/Users/Public/insurance_Sell2.txt"

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

def cancel_SellStop_order():
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_STOP and order.state == mt5.ORDER_STATE_PLACED:
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
    price = startPrice - position * points     # Set the price for the Buy Limit order
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

def sellStop(position, volume):
    symbol = "EURUSD"  # Replace with the desired symbol
    order_type = mt5.ORDER_TYPE_SELL_STOP
    price = startPrice - position * points
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
        print("Sell Stop order placed successfully. Order ticket:", result.order)

def sellLimit(position, volume):
    symbol = "EURUSD"  # Replace with the desired symbol
    order_type = mt5.ORDER_TYPE_SELL_LIMIT
    price = startPrice - position * points
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
  
def blackSellLimit(position, volume):
    symbol = "EURUSD"  # Replace with the desired symbol
    order_type = mt5.ORDER_TYPE_SELL_LIMIT
    price = startPrice - position * points
    stop_loss = price + points*2  # Replace with the desired stop loss price
    take_profit = price - points*3  # Replace with the desired take profit price

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
        print("Sell Stop order placed successfully. Order ticket:", result.order)

def blackbuyLimit(position, volume):
    symbol = "EURUSD"  # EUR/USD currency pair
    order_type = mt5.ORDER_TYPE_BUY_LIMIT       # Replace with the desired volume/lot size
    price = startPrice - position * points     # Set the price for the Buy Limit order
    stop_loss = price - points*2  # Replace with the desired stop loss price
    take_profit = price + points*3  # Replace with the desired take profit price
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
        print("Buy LImit Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Limit order placed successfully. Order ticket:", result.order)
first_active = False
second_active = False
third_active = False
fourd_active = False
fifth_active = False
sixth_active = False

third = False
fourd = False
fifth = False
sixth = False

sellStop(0, volume)

once = False
while failed == False and succes == False:

    last_price = mt5.symbol_info_tick(symbol).ask

    if(last_price <= startPrice and once == False):
        first_active = True
        sellStop(1, volume*2)
        once = True
    
    if(first_active and last_price >= startPrice + points):
        failed = True
        cancel_SellStop_order()

    if(first_active and last_price <= startPrice - points):
        first_active = False
        second_active = True

    if(second_active and last_price >= startPrice):
        failed = True
        cancel_buyLimit_order()

    if(second_active and last_price <= startPrice - points*2):
        second_active = False
        third_active = True

    if(third_active and last_price <= startPrice - points*3):
        failed = True
        cancel_buyStop_order()
    
    if(third_active and last_price >= startPrice - points):
        third_active = False
        fourd_active = True

    if(fourd_active and last_price >= startPrice):
        failed = True
        cancel_buyLimit_order()

    if(fourd_active and last_price <= startPrice - points*2):
        fifth_active = True
        fourd_active = False
    
    if(fifth_active and last_price <= startPrice - points*4):
        failed = True
        fifth_active = False

    if(fifth_active and last_price >= startPrice + points):
        fifth_active = False
        succes = True

        

    if(failed == False):

        if(last_price <= startPrice - points and third == False and second_active):    
            buyLimit(2, volume*4)
            third = True
        if(last_price <= startPrice - points*2 and fourd == False and third_active):
            sellLimit(1, volume*8)
            fourd = True
        if(last_price >= startPrice - points and fifth == False and fourd_active):
            blackbuyLimit(2,black_volume)
            fifth = True
        
        
        
        
        

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