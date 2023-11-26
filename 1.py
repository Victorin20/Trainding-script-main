import MetaTrader5 as mt5
import time
mt5.initialize()

#startPrice > actual Price

symbol = "EURUSD"
points = 0.0005
startPrice = 1.0737

volume_1 = 0.07


failed_1 = False

succes = False
failures = 0

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

def cancel_buyLimit_order(combination_number):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_LIMIT and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order 
                break
    if(order_to_remove != None):
        cancel_order(order_to_remove.ticket)
        print("BuyLimit order removed")

def cancel_SellStop_order(combination_number):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_STOP and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order
                break
    if(order_to_remove != None):            
        cancel_order(order_to_remove.ticket)
        print("SellStop order removed")

def cancel_SellLimit_order(combination_number):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_LIMIT and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order
                break
    if(order_to_remove != None):            
        cancel_order(order_to_remove.ticket)
        print("SellLimit order removed")

def cancel_buyStop_order(combination_number):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_STOP and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order 
                break
    if(order_to_remove != None):
        cancel_order(order_to_remove.ticket)
        print("BuyStop order removed")
          
def buyLimit(position, volume, combination_number):
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
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Buy Limit Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Limit order placed successfully. Order ticket:", result.order)

def buyStop(position, volume, combination_number):
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
    "comment": str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Buy Stop Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Stop order placed successfully. Order ticket:", result.order)

def sellStop(position, volume, combination_number):
    order_type = mt5.ORDER_TYPE_SELL_STOP
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
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Sell Stop Order placement failed. Error code:", result.retcode)
    else:
        print("Sell Stop order placed successfully. Order ticket:", result.order)

def sellLimit(position, volume, combination_number):
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
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("SellLimit Order placement failed. Error code:", result.retcode)
    else:
        print("SellLimit order placed successfully. Order ticket:", result.order)
        
def blackbuyLimit(position, volume, stoploss, takeprofit, combination_number):
    order_type = mt5.ORDER_TYPE_BUY_LIMIT
    price = startPrice + position * points
    stop_loss = price + stoploss  # Replace with the desired stop loss price
    take_profit = price - takeprofit  # Replace with the desired take profit price

    request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": volume,
    "type": order_type,
    "price": price,
    "sl": stop_loss,
    "tp": take_profit,
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("BlackSellLimit Order placement failed. Error code:", result.retcode)
    else:
        print("BlackSellLimit order placed successfully. Order ticket:", result.order)

first_active_1 = False
second_active_1 = False
third_active_1  = False
fourd_active_1  = False
fifth_active_1  = False
sixth_active_1  = False

third_1 = False
fourd_1 = False
fifth_1 = False
sixth_1 = False

once = False

print("Sell1-11 Start")
#combination 1
buyLimit(0, volume_1, 1)

fail = 0

x = 0

while fail != 1 and succes == False:
   
    last_price = mt5.symbol_info_tick(symbol).ask

    time.sleep(3)
    if(last_price <= startPrice and once == False):

        first_active_1 = True
        sellLimit(1, volume_1*2, 1)
        once = True

    #combination 1

    if(failed_1 == False):
        
        if(first_active_1 and last_price <= round(startPrice - points, 5)):
            failed_1 = True
            first_active_1 = False
            cancel_SellLimit_order(1)

        if(first_active_1 and last_price >= round(startPrice + points,5)):
            first_active_1 = False
            second_active_1 = True

        if(second_active_1 and last_price >= round(startPrice + points*2,5)):
            failed_1 = True
            second_active_1 = False
            cancel_buyLimit_order(1)

        if(second_active_1 and last_price <= round(startPrice, 5)):
            second_active_1 = False
            third_active_1 = True

        if(third_active_1 and last_price <= round(startPrice - points,5)):
            failed_1 = True
            third_active_1 = False
            cancel_buyStop_order(1)
        
        if(third_active_1 and last_price >= round(startPrice + points,5)):
            third_active_1 = False
            fourd_active_1 = True
        
        if(fourd_active_1 and last_price <= round(startPrice,5)):
            failed_1 = True
            fourd_active_1 = False
            cancel_buyStop_order(1)

        if(fourd_active_1 and last_price >= round(startPrice + points*2,5)):
            fourd_active_1 = False
            fifth_active_1 = True

        if(fifth_active_1 and last_price <= round(startPrice + points,5)):
            failed_1 = True
            fifth_active_1 = False
            cancel_buyStop_order(1)

        if(fifth_active_1 and last_price >= round(startPrice + points*3, 5)):
            fifth_active_1 = False
            sixth_active_1 = True
        
        if(sixth_active_1 and last_price <= round(startPrice + points*2, 5)):
            failed_1 = True
            sixth_active_1 = False

        if(sixth_active_1 and last_price >= round(startPrice + points*4, 5)):
            sixth_active_1 = False
            print("Sell combination 1 finished")
            succes = True

        if(failed_1 == False):

            if(last_price >= round(startPrice + points, 5) and third_1 == False and second_active_1):    
                buyLimit(0, volume_1*4, 1)
                third_1 = True

            if(last_price <= round(startPrice, 5) and fourd_1 == False and third_active_1):
                buyStop(1, volume_1*8, 1)
                fourd_1 = True
        else :
            print("Sell Combination 1 failed")
            fail += 1
    
   

if(succes):
    print("Succes")
else :
    print("Failed")

mt5.shutdown()