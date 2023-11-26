import MetaTrader5 as mt5
import time
mt5.initialize()

symbol = "EURUSD"
startPrice = 1.0707
volume = 0.01
points = 0.0005
startPoints = 0.0005

failed = False
succes = False

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

def cancel_buyStop_order():
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_STOP and order.state == mt5.ORDER_STATE_PLACED:
            order_to_remove = order
            break
    if(order_to_remove != None):
        cancel_order(order_to_remove.ticket)
        print("BuyStop order removed")

def buyStop(position, volume):
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

def buyLimit(position, volume):
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
        print("Buy Limit Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Limit order placed successfully. Order ticket:", result.order)

def buyLimitStart(position, volume):
    order_type = mt5.ORDER_TYPE_BUY_LIMIT       # Replace with the desired volume/lot size
    price = startPrice + position * startPoints     # Set the price for the Buy Limit order
    stop_loss = price - startPoints  # Replace with the desired stop loss price
    take_profit = price + startPoints  # Replace with the desired take profit price
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
        print("Buy Limit Order placement failed. Error code:", result.retcode)
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

once = False

print("Buy12 start")
buyLimitStart(0, volume)

while failed == False and succes == False:

    time.sleep(0.1)

    last_price = mt5.symbol_info_tick(symbol).ask

    if(last_price <= startPrice and once == False):
        first_active = True
        buyStop(1, volume*2)
        once = True
        
    if(first_active and last_price >= round(startPrice + points,5)):
        failed = True
        first_active = False
        cancel_buyStop_order()

    if(first_active and last_price <= round(startPrice - points,5)):
        first_active = False
        second_active = True

    if(second_active and last_price >= round(startPrice,5)):
        failed = True
        second_active = False
        cancel_buyStop_order()

    if(second_active and last_price <= round(startPrice - points*2,5)):
        second_active = False
        third_active = True

    if(third_active and last_price >= round(startPrice - points,5)):
        failed = True
        third_active = False
        cancel_buyStop_order()
    
    if(third_active and last_price <= round(startPrice - points*3,5)):
        third_active = False
        fourd_active = True
    
    if(fourd_active and last_price >= round(startPrice - points*2,5)):
        failed = True
        fourd_active = False

    if(fourd_active and last_price <= round(startPrice - points*4,5)):
        fourd_active = False
        print("Buy combination 12 finished")
        succes = True

    if(failed == False):

        if(last_price <= round(startPrice - points,5) and third == False and second_active):    
            buyStop(2, volume*4)
            third = True

        if(last_price <= round(startPrice - points*2,5) and fourd == False and third_active):
            buyStop(3, volume*8)
            fourd = True


if(succes):
    print("Succes you win")
else : 
    print("buy combination 12 failed")
 
mt5.shutdown()