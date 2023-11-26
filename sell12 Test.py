import MetaTrader5 as mt5
import time
mt5.initialize()

symbol = "EURUSD"
startPrice = 1.07000
volume = 0.27
points = 0.0025

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

def cancel_SellStop_order():
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_STOP and order.state == mt5.ORDER_STATE_PLACED:
            order_to_remove = order
            break
    if(order_to_remove != None):
        cancel_order(order_to_remove.ticket)
        print("SellStop order removed")

def sellStop(position, volume):
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
        print("Sell Stop Order placement failed. Error code:", result.retcode)
    else:
        print("Sell Stop order placed successfully. Order ticket:", result.order)
  
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

print("Sell12 start")
sellStop(0, volume)
x = 0
last_price = startPrice
while failed == False and succes == False:

    if(x == 1):
        last_price += points
        last_price = round(last_price, 5)
        print("2")
    if(x == 2):
        last_price += points
        last_price = round(last_price, 5)
        print("3")
    '''if(x == 3):
        last_price -= points
        last_price = round(last_price, 5)
        print("4")
    if(x == 4):
        last_price -= points
        last_price = round(last_price, 5)
        print("5")
    if(x == 5):
        last_price -= points
        last_price = round(last_price, 5)
        print("6")
    if(x == 6):
        last_price -= points
        last_price = round(last_price, 5)
        print("7")
    if(x == 7):
        last_price -= points*2
        last_price = round(last_price, 5)'''

    x += 1

    if(last_price <= startPrice and once == False):
        first_active = True
        sellStop(1, volume*2)
        once = True
        
    if(first_active and last_price >= round(startPrice + points,5)):
        failed = True
        first_active = False
        cancel_SellStop_order()

    if(first_active and last_price <= round(startPrice - points,5)):
        first_active = False
        second_active = True
        cancel_SellStop_order()

    if(second_active and last_price >= round(startPrice,5)):
        failed = True
        second_active = False
        cancel_SellStop_order()

    if(second_active and last_price <= round(startPrice - points*2,5)):
        second_active = False
        third_active = True
        cancel_SellStop_order()

    if(third_active and last_price >= round(startPrice - points,5)):
        failed = True
        third_active = False
        cancel_SellStop_order()
    
    if(third_active and last_price <= round(startPrice - points*3,5)):
        third_active = False
        fourd_active = True
        cancel_SellStop_order()
    
    if(fourd_active and last_price >= round(startPrice - points*2,5)):
        failed = True
        fourd_active = False

    if(fourd_active and last_price <= round(startPrice - points*4,5)):
        fourd_active = False
        print("Sell combination 12 finished")
        succes = True

    if(failed == False):

        if(last_price <= round(startPrice - points,5) and third == False and second_active):    
            sellStop(2, volume*4)
            third = True

        if(last_price <= round(startPrice - points*2,5) and fourd == False and third_active):
            sellStop(3, volume*8)
            fourd = True


if(succes):
    print("Succes you win")
else : 
    print("Sell combination 12 failed")
 
mt5.shutdown()