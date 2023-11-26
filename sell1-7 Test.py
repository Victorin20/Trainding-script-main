import MetaTrader5 as mt5
import time
mt5.initialize()

#startPrice < actual Price

symbol = "EURUSD"
points = 0.0010
startPrice = 1.054

volume_1 = 0.01
black_volume_1 = 0.03
volume_2 = 0.05
black_volume_2 = 0.4
volume_3 = 0.03
black_volume_3 = 0.03
volume_4 = 0.04
black_volume_4 = 0.03
volume_5 = 0.05
black_volume_5 = 0.8
volume_6 = 0.06
black_volume_6 = 0.8
volume_7 = 0.07
black_volume_7 = 0.4


failed_1 = False
failed_2 = False
failed_3 = False
failed_4 = False
failed_5 = False
failed_6 = False
failed_7 = False

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

def cancel_buyLimit_order(combination_number, step):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_LIMIT and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order 
                break
    if(order_to_remove != None):
        cancel_order(order_to_remove.ticket)
        print("BuyLimit  " + str(step) + "  order removed for  " + str(combination_number) + "  combination")

def cancel_SellStop_order(combination_number,step):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_STOP and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order
                break
    if(order_to_remove != None):            
        cancel_order(order_to_remove.ticket)
        print("SellStop  " + str(step) + "  order removed for " + str(combination_number) + "  combination")

def cancel_SellLimit_order(combination_number,step):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_SELL_LIMIT and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order
                break
    if(order_to_remove != None):            
        cancel_order(order_to_remove.ticket)
        print("SellLimit  " + str(step) + " order removed for  " + str(combination_number) + " combination")

def cancel_buyStop_order(combination_number, step):
    orders = mt5.orders_get(only_this_symbol=False)

    order_to_remove = None
    for order in orders:
        if order.type == mt5.ORDER_TYPE_BUY_STOP and order.state == mt5.ORDER_STATE_PLACED:
            if(order.comment == str(combination_number)):
                order_to_remove = order 
                break
    if(order_to_remove != None):
        cancel_order(order_to_remove.ticket)
        print("BuyStop  " + str(step) + "  order removed for  " + str(combination_number) + " combination")
          
def buyLimit(position, volume, combination_number):
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
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Buy Limit Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Limit order placed successfully. Order ticket:", result.order)

def buyStop(position, volume, combination_number):
    order_type = mt5.ORDER_TYPE_BUY_STOP       # Replace with the desired volume/lot size
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
    "comment": str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Buy Stop Order placement failed. Error code:", result.retcode)
    else:
        print("Buy Stop order placed successfully. Order ticket:", result.order)

def sellStop(position, volume, combination_number):
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
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Sell Stop Order placement failed. Error code:", result.retcode)
    else:
        print("Sell Stop order placed successfully. Order ticket:", result.order)

def sellLimit(position, volume, combination_number):
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
    "comment":str(combination_number),
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("SellLimit Order placement failed. Error code:", result.retcode)
    else:
        print("SellLimit order placed successfully. Order ticket:", result.order)
        
def blackSellLimit(position, volume, stoploss, takeprofit, combination_number):
    order_type = mt5.ORDER_TYPE_SELL_LIMIT
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


first_active_2 = False
second_active_2 = False
third_active_2 = False
fourd_active_2 = False


first_active_3 = False
second_active_3 = False
third_active_3  = False
fourd_active_3  = False
fifth_active_3  = False

first_active_4 = False
second_active_4 = False
third_active_4 = False
fourd_active_4 = False
fifth_active_4 = False
sixth_active_4 = False

first_active_5 = False
second_active_5 = False
third_active_5 = False
fourd_active_5 = False
fifth_active_5 = False
sixth_active_5 = False
seventh_active_5 = False

first_active_6 = False
second_active_6 = False
third_active_6 = False
fourd_active_6 = False
fifth_active_6 = False
sixth_active_6 = False
seventh_active_6 = False
eight_active_6 = False

first_active_7 = False
second_active_7 = False
third_active_7 = False
fourd_active_7 = False
fifth_active_7 = False
sixth_active_7 = False
seventh_active_7 = False
eight_active_7 = False
nine_active_7 = False

third_1 = False

third_2 = False
fourd_2 = False

third_3 = False
fourd_3 = False
fifth_3 = False

third_4 = False
fourd_4 = False
fifth_4 = False
sixth_4 = False

third_5 = False
fourd_5 = False
fifth_5 = False
sixth_5 = False
seventh_5 = False

third_6 = False
fourd_6 = False
fifth_6 = False
sixth_6 = False
seventh_6 = False
eight_6 = False

third_7 = False
fourd_7 = False
fifth_7 = False
sixth_7 = False
seventh_7 = False
eight_7 = False
nine_7 = False

once = False

print("Sell1-7 Start")
#combination 1
sellStop(0, volume_1, 1)

#combination 2
sellStop(0, volume_2, 2)

#combination 3
sellStop(0, volume_3, 3)

#combination 4
sellStop(0, volume_4, 4)

#combination 5
sellStop(0, volume_5, 5)

#combination 6
sellStop(0, volume_6, 6)

#combination 7
sellStop(0, volume_7, 7)

fail = 0
last_price = startPrice
x = 0
while fail != 11 and succes == False:
   
    #last_price = mt5.symbol_info_tick(symbol).ask
    if(x == 1):
        last_price -= points
        last_price = round(last_price, 5)
        print("2")
    if(x == 2):
        last_price -= points
        last_price = round(last_price, 5)
        print("3")
    if(x == 3):
        last_price -= points
        last_price = round(last_price, 5)
        print("4")
    if(x == 4):
        last_price -= points
        last_price = round(last_price, 5)
        print("5")
    '''if(x == 5):
        last_price -= points
        last_price = round(last_price, 5)
        print("6")
    if(x == 6):
        last_price -= points*7
        last_price = round(last_price, 5)
        print("7")
    if(x == 7):
        last_price += points*2
        last_price = round(last_price, 5)'''

    x += 1
  
    if(last_price <= startPrice and once == False):

        first_active_1 = True
        first_active_2 = True
        first_active_3 = True
        first_active_4 = True
        first_active_5 = True
        first_active_6 = True
        first_active_7 = True
        buyLimit(1, volume_1*2, 1)
        sellStop(1, volume_2*2, 2)
        sellStop(1, volume_3*2, 3)
        sellStop(1, volume_4*2, 4)
        sellStop(1, volume_5*2, 5)
        sellStop(1, volume_6*2, 6)
        sellStop(1, volume_7*2, 7)
        cancel_SellStop_order(1,2)
        cancel_SellStop_order(2,2)
        cancel_SellStop_order(3,2)
        cancel_SellStop_order(4,2)
        cancel_SellStop_order(5,2)
        cancel_SellStop_order(6,2)
        cancel_SellStop_order(7,2)
  
        once = True

    #combination 1

    if(failed_1 == False):
        
        if(first_active_1 and last_price >= round(startPrice + points, 5)):
            failed_1 = True
            first_active_1 = False
            cancel_buyLimit_order(1, 1)

        if(first_active_1 and last_price <= round(startPrice - points,5)):
            first_active_1 = False
            second_active_1 = True
            cancel_buyLimit_order(1, 1)

        if(second_active_1 and last_price <= round(startPrice - points*2,5)):
            failed_1 = True
            second_active_1 = False
            cancel_SellLimit_order(1, 2)

        if(second_active_1 and last_price >= round(startPrice, 5)):
            second_active_1 = False
            third_active_1 = True
            cancel_SellLimit_order(1, 2)

        if(third_active_1 and last_price >= round(startPrice + points,5)):
            failed_1 = True
            third_active_1 = False

        if(third_active_1 and last_price <= round(startPrice - points*8, 5)):
            third_active_1 = False
            print("Sell combination 1 finished")
            succes = True

        if(failed_1 == False):

            if(last_price <= round(startPrice - points, 5) and third_1 == False and second_active_1):    
                blackSellLimit(0, black_volume_1, points*1, points*8, 1)
                third_1 = True
        else :
            print("Sell Combination 1 failed")
            fail += 1
    
    #combination 2

    if(failed_2 == False):

        if(first_active_2 and last_price >= round(startPrice + points, 5)):
            failed_2 = True
            first_active_2 = False
            cancel_SellStop_order(2, 1)

        if(first_active_2 and last_price <= round(startPrice - points,5)):
            first_active_2 = False
            second_active_2 = True
            cancel_SellStop_order(2, 1)

        if(second_active_2 and last_price >= round(startPrice,5)):
            failed_2 = True
            second_active_2 = False
            cancel_buyLimit_order(2, 2)

        if(second_active_2 and last_price <= round(startPrice - points*2, 5)):
            second_active_2 = False
            third_active_2 = True
            cancel_buyLimit_order(2, 2)

        if(third_active_2 and last_price <= round(startPrice - points*3,5)):
            failed_2 = True
            third_active_2 = False
            cancel_SellLimit_order(2, 3)

        if(third_active_2 and last_price >= round(startPrice - points, 5)):
            third_active_2 = False
            fourd_active_2 = True
            cancel_SellLimit_order(2, 3)
        
        if(fourd_active_2 and last_price >= round(startPrice + points,5)):
            failed_2 = True
            fourd_active_2 = False
            
        if(fourd_active_2 and last_price <= round(startPrice - points*8,5)):   
            print("Sell combination 2 finished")
            succes = True

        if(failed_2 == False):

            if(last_price <= round(startPrice - points, 5) and third_2 == False and second_active_2):    
                buyLimit(2, volume_2*2, 2)
                third_2 = True

            if(last_price <= round(startPrice - points*2, 5) and fourd_2 == False and third_active_2):    
                blackSellLimit(1, black_volume_2, points*2, points*7, 2)
                fourd_2 = True
        else :
            print("Sell Combination 2 failed")
            fail += 1
    #combination 3

    if(failed_3 == False):

        if(first_active_3 and last_price >= round(startPrice + points,5)):
            failed_3 = True
            first_active_3 = False
            cancel_SellStop_order(3, 1)

        if(first_active_3 and last_price <= round(startPrice - points,5)):
            first_active_3 = False
            second_active_3 = True
            cancel_SellStop_order(3, 1)

        if(second_active_3 and last_price >= round(startPrice,5)):
            failed_3 = True
            second_active_3 = False
            cancel_SellStop_order(3,2)

        if(second_active_3 and last_price <= round(startPrice - points *2,5)):
            second_active_3 = False
            third_active_3 = True
            cancel_SellStop_order(3,2)

        if(third_active_3 and last_price >= round(startPrice - points,5)):
            failed_3 = True
            third_active_3 = False
            cancel_buyLimit_order(3,3)
        
        if(third_active_3 and last_price <= round(startPrice - points*3,5)):
            third_active_3 = False
            fourd_active_3 = True
            cancel_buyLimit_order(3,3)
        
        if(fourd_active_3 and last_price <= round(startPrice - points*4,5)):
            failed_3 = True
            fourd_active_3 = False
            cancel_SellLimit_order(3,4)

        if(fourd_active_3 and last_price >= round(startPrice - points*2,5)):
            fourd_active_3 = False
            fifth_active_3 = True
            cancel_SellLimit_order(3,4)

        if(fifth_active_3 and last_price >= round(startPrice + points,5)):
            failed_3 = True
            fifth_active_3 = False

        if(fifth_active_3 and last_price <= round(startPrice - points*8,5)):
            fifth_active_3 = False
            print("Sell combination 3 finished")
            succes = True

        if(failed_3 == False):

            if(last_price <= round(startPrice - points, 5) and third_3 == False and second_active_3):    
                sellStop(2, volume_3*2, 3)
                third_3 = True

            if(last_price <= round(startPrice - points*2, 5) and fourd_3 == False and third_active_3):    
                buyLimit(3, volume_3*4, 3)
                fourd_3 = True

            if(last_price <= round(startPrice - points*3, 5) and fifth_3 == False and fourd_active_3):    
                blackSellLimit(2, black_volume_3,points*3, points*6, 3)
                fifth_3 = True

        else :
            print("Sell Combination 3 failed")
            fail += 1
    #combination 4

    if(failed_4 == False):

        if(first_active_4 and last_price >= round(startPrice + points,5)):
            failed_4 = True
            first_active_4 = False
            cancel_SellStop_order(4,1)

        if(first_active_4 and last_price <= round(startPrice - points,5)):
            first_active_4 = False
            second_active_4 = True
            cancel_SellStop_order(4,1)

        if(second_active_4 and last_price >= round(startPrice,5)):
            failed_4 = True
            second_active_4 = False
            cancel_SellStop_order(4,2)

        if(second_active_4 and last_price <= round(startPrice - points*2,5)):
            second_active_4 = False
            third_active_4 = True
            cancel_SellStop_order(4,2)

        if(third_active_4 and last_price >= round(startPrice - points,5)):
            failed_4 = True
            third_active_4 = False
            cancel_SellStop_order(4,3)
        
        if(third_active_4 and last_price <= round(startPrice - points*3,5)):
            third_active_4 = False
            fourd_active_4 = True
            cancel_SellStop_order(4,3)
        
        if(fourd_active_4 and last_price >= round(startPrice-points*2,5)):
            failed_4 = True
            fourd_active_4 = False
            cancel_buyLimit_order(4,4)

        if(fourd_active_4 and last_price <= round(startPrice - points*4,5)):
            fourd_active_4 = False
            fifth_active_4 = True
            cancel_buyLimit_order(4,4)

        if(fifth_active_4 and last_price <= round(startPrice - points*5,5)):
            failed_4 = True
            fifth_active_4 = False
            cancel_SellLimit_order(4,5)

        if(fifth_active_4 and last_price >= round(startPrice - points*3,5)):
            fifth_active_4 = False
            sixth_active_4 = True
            cancel_SellLimit_order(4,5)
        
        if(sixth_active_4 and last_price >= round(startPrice + points,5)):
            failed_4 = True
            sixth_active_4 = False

        if(sixth_active_4 and last_price <= round(startPrice - points*8,5)):
            sixth_active_4 = False
            print("Sell combination 4 finished")
            succes = True

        if(failed_4 == False):

            if(last_price <= round(startPrice - points,5) and third_4 == False and second_active_4):    
                sellStop(2, volume_4*4, 4)
                third_4 = True

            if(last_price <= round(startPrice - points*2,5) and fourd_4 == False and third_active_4):
                sellStop(3, volume_4*8, 4)
                fourd_4 = True
            
            if(last_price <= round(startPrice - points*3,5) and fifth_4 == False and fourd_active_4):
                buyLimit(4, volume_4*16, 4)
                fifth_4 = True
            
            if(last_price <= round(startPrice - points*4,5) and sixth_4 == False and fifth_active_4):
                blackSellLimit(3, black_volume_4,points*4, points*5, 5)
                sixth_4 = True
        else :
            print("Sell Combination 4 failed")
            fail += 1

    #combination 5

    if(failed_5 == False):
        
        if(first_active_5 and last_price >= round(startPrice + points,5)):
            failed_5 = True
            first_active_5 = False
            cancel_SellStop_order(5,1)

        if(first_active_5 and last_price <= round(startPrice - points,5)):
            first_active_5 = False
            second_active_5 = True
            cancel_SellStop_order(5,1)

        if(second_active_5 and last_price >= round(startPrice,5)):
            failed_5 = True
            second_active_5 = False
            cancel_SellStop_order(5,2)

        if(second_active_5 and last_price <= round(startPrice - points*2,5)):
            second_active_5 = False
            third_active_5 = True
            cancel_SellStop_order(5,2)

        if(third_active_5 and last_price >= round(startPrice - points,5)):
            failed_5 = True
            third_active_5 = False
            cancel_SellStop_order(5,3)
        
        if(third_active_5 and last_price <= round(startPrice - points*3,5)):
            third_active_5 = False
            fourd_active_5 = True
            cancel_SellStop_order(5,3)
        
        if(fourd_active_5 and last_price >= round(startPrice - points*2,5)):
            failed_5 = True
            fourd_active_5 = False
            cancel_SellStop_order(5,4)

        if(fourd_active_5 and last_price <= round(startPrice - points*4,5)):
            fourd_active_5 = False
            fifth_active_5 = True
            cancel_SellStop_order(5,4)

        if(fifth_active_5 and last_price >= round(startPrice - points*3,5)):
            failed_5 = True
            fifth_active_5 = False
            cancel_buyLimit_order(5,5)

        if(fifth_active_5 and last_price <= round(startPrice - points*5,5)):
            fifth_active_5 = False
            sixth_active_5 = True
            cancel_buyLimit_order(5,5)
        
        if(sixth_active_5 and last_price <= round(startPrice - points*6,5)):
            failed_5 = True
            sixth_active_5 = False
            cancel_SellLimit_order(5,6)

        if(sixth_active_5 and last_price >= round(startPrice - points*4,5)):
            sixth_active_5 = False
            seventh_active_5 = True
            cancel_SellLimit_order(5,6)

        if(seventh_active_5 and last_price >= round(startPrice + points,5)):
            failed_5 = True
            seventh_active_5 = False

        if(seventh_active_5 and last_price <= round(startPrice - points*8,5)):    
            seventh_active_5 = False
            print("Sell comtination 5 finished")
            succes = True

        if(failed_5 == False):

            if(last_price <= round(startPrice - points,5) and third_5 == False and second_active_5):    
                sellStop(2, volume_5*4, 5)
                third_5 = True

            if(last_price <= round(startPrice-points*2,5) and fourd_5 == False and third_active_5):
                sellStop(3, volume_5*8, 5)
                fourd_5 = True
            
            if(last_price <= round(startPrice - points*3,5) and fifth_5 == False and fourd_active_5):
                sellStop(4, volume_5*16, 5)
                fifth_5 = True
            
            if(last_price <= round(startPrice - points * 4,5) and sixth_5 == False and fifth_active_5):
                buyLimit(5, volume_5*32, 5)
                sixth_5 = True

            if(last_price <= round(startPrice - points * 5,5) and seventh_5 == False and sixth_active_5):
                blackSellLimit(4, black_volume_5,points*5, points*4, 5)
                seventh_5 = True
            
        else :
            print("Sell Combination 5 failed")
            fail += 1
    #combination 6

    if(failed_6 == False):

        if(first_active_6 and last_price >= round(startPrice + points,5)):
            failed_6 = True
            first_active_6 = False
            cancel_SellStop_order(6,1)

        if(first_active_6 and last_price <= round(startPrice - points,5)):
            first_active_6 = False
            second_active_6 = True
            cancel_SellStop_order(6,1)

        if(second_active_6 and last_price >= round(startPrice,5)):
            failed_6 = True
            second_active_6 = False
            cancel_SellStop_order(6,2)

        if(second_active_6 and last_price <= round(startPrice - points*2,5)):
            second_active_6 = False
            third_active_6 = True
            cancel_SellStop_order(6,2)

        if(third_active_6 and last_price >= round(startPrice - points,5)):
            failed_6 = True
            third_active_6 = False
            cancel_SellStop_order(6,3)
        
        if(third_active_6 and last_price <= round(startPrice - points*3,5)):
            third_active_6 = False
            fourd_active_6 = True
            cancel_SellStop_order(6,3)
        
        if(fourd_active_6 and last_price >= round(startPrice - points*2,5)):
            failed_6 = True
            fourd_active_6 = False
            cancel_SellStop_order(6,4)

        if(fourd_active_6 and last_price <= round(startPrice - points*4,5)):
            fourd_active_6 = False
            fifth_active_6 = True
            cancel_SellStop_order(6,4)

        if(fifth_active_6 and last_price >= round(startPrice - points*3,5)):
            failed_6 = True
            fifth_active_6 = False
            cancel_SellStop_order(6,5)

        if(fifth_active_6 and last_price <= round(startPrice - points*5,5)):
            fifth_active_6 = False
            sixth_active_6 = True
            cancel_SellStop_order(6,5)
        
        if(sixth_active_6 and last_price >= round(startPrice - points*4,5)):
            failed_6 = True
            sixth_active_6 = False
            cancel_buyLimit_order(6,6)

        if(sixth_active_6 and last_price <= round(startPrice - points*6,5)):
            sixth_active_6 = False
            seventh_active_6 = True
            cancel_buyLimit_order(6,6)
        
        if(seventh_active_6 and last_price <= round(startPrice - points*7,5)):
            failed_6 = True
            seventh_active_6 = False
            cancel_SellLimit_order(6,7)

        if(seventh_active_6 and last_price >= round(startPrice - points*5,5)):
            seventh_active_6 = False
            eight_active_6 = True
            cancel_SellLimit_order(6,7)
        
        if(eight_active_6 and last_price >= round(startPrice +points,5)):
            failed_6 = True
            eight_active_6 = False
        
        if(eight_active_6 and last_price <= round(startPrice -points*8,5)):
            eight_active_6 = False
            succes = True
            print("Sell comtination 6 finished")
                  

        if(failed_6 == False):

            if(last_price <= round(startPrice - points,5) and third_6 == False and second_active_6):    
                sellStop(2, volume_6*4, 6)
                third_6 = True

            if(last_price <= round(startPrice - points*2,5) and fourd_6 == False and third_active_6):
                sellStop(3, volume_6*8, 6)
                fourd_6 = True
            
            if(last_price <= round(startPrice - points*3,5) and fifth_6 == False and fourd_active_6):
                sellStop(4, volume_6*16, 6)
                fifth_6 = True
            
            if(last_price <= round(startPrice - points*4,5) and sixth_6 == False and fifth_active_6):
                sellStop(5, volume_6*32, 6)
                sixth_6 = True
            
            if(last_price <= round(startPrice - points*5,5) and seventh_6 == False and sixth_active_6):
                buyLimit(6, volume_6*64, 6)
            
            if(last_price <= round(startPrice - points*6,5) and eight_6 == False and seventh_active_6):
                blackSellLimit(5, black_volume_6, points*6, points*3, 6)
                eight_6 = True
        else :
            print("Sell Combination 6 failed")
            fail += 1
    #combination 7

    if(failed_7 == False):

        if(first_active_7 and last_price >= round(startPrice + points,5)):
            failed_7 = True
            first_active_7 = False
            cancel_SellStop_order(7,1)

        if(first_active_7 and last_price <= round(startPrice - points,5)):
            first_active_7 = False
            second_active_7 = True
            cancel_SellStop_order(7,1)

        if(second_active_7 and last_price >= round(startPrice,5)):
            failed_7 = True
            second_active_7 = False
            cancel_SellStop_order(7,2)

        if(second_active_7 and last_price <= round(startPrice - points*2,5)):
            second_active_7 = False
            third_active_7 = True
            cancel_SellStop_order(7,2)

        if(third_active_7 and last_price >= round(startPrice - points,5)):
            failed_7 = True
            third_active_7 = False
            cancel_SellStop_order(7,3)
        
        if(third_active_7 and last_price <= round(startPrice - points*3,5)):
            third_active_7 = False
            fourd_active_7 = True
            cancel_SellStop_order(7,3)
        
        if(fourd_active_7 and last_price >= round(startPrice - points*2,5)):
            failed_7 = True
            fourd_active_7 = False
            cancel_SellStop_order(7,4)

        if(fourd_active_7 and last_price <= round(startPrice - points*4,5)):
            fourd_active_7 = False
            fifth_active_7 = True
            cancel_SellStop_order(7,4)

        if(fifth_active_7 and last_price >= round(startPrice - points * 3,5)):
            failed_7 = True
            fifth_active_7 = False
            cancel_SellStop_order(7,5)

        if(fifth_active_7 and last_price <= round(startPrice - points*5,5)):
            fifth_active_7 = False
            sixth_active_7 = True
            cancel_SellStop_order(7,5)
        
        if(sixth_active_7 and last_price >= round(startPrice - points*4,5)):
            failed_7 = True
            sixth_active_7 = False
            cancel_SellStop_order(7,6)
        
        if(sixth_active_7 and last_price <= round(startPrice - points*6,5)):
            sixth_active_7 = False
            seventh_active_7 = True
            cancel_SellStop_order(7,6)
        
        if(seventh_active_7 and last_price >= round(startPrice - points*5,5)):
            seventh_active_7 = False
            failed_7 = True
            cancel_buyLimit_order(7,7)

        if(seventh_active_7 and last_price <= round(startPrice - points*7,5)):
            seventh_active_7 = False
            eight_active_7 = True
            cancel_buyLimit_order(7,7)

        if(eight_active_7 and last_price <= round(startPrice - points*8,5)):
            failed_7 = True
            eight_active = False
            cancel_SellLimit_order(7,8)

        if(eight_active_7 and last_price >= round(startPrice-points*6,5)):
           eight_active_7 = False
           nine_active_7 = True
           cancel_SellLimit_order(7,8)

        if(nine_active_7 and last_price >= round(startPrice + points,5)):
            nine_active_7 = False
            failed_7 = True

        if(nine_active_7 and last_price <= round(startPrice - points*8,5)):
            nine_active_7 = False
            print("Sell combination 7 finished")
            succes= True
    
        if(failed_7 == False):

            if(last_price <= round(startPrice - points,5) and third_7 == False and second_active_7):    
                sellStop(2, volume_7*4, 7)
                third_7 = True

            if(last_price <= round(startPrice - points*2,5) and fourd_7 == False and third_active_7):
                sellStop(3, volume_7*8, 7)
                fourd_7 = True

            if(last_price <= round(startPrice - points*3,5) and fifth_7 == False and fourd_active_7):
                sellStop(4, volume_7*16, 7)
                fifth_7 = True

            if(last_price <= round(startPrice - points*4,5) and sixth_7 == False and fifth_active_7):
                sellStop(5, volume_7*32, 7)
                sixth_7 = True

            if(last_price <= round(startPrice - points*5,5) and seventh_7 == False and sixth_active_7):
                sellStop(6, volume_7*64, 7)
                seventh_7 = True

            if(last_price <= round(startPrice - points*6,5) and eight_7 == False and seventh_active_7):
                buyLimit(7, volume_7*128, 7)
                eight_7 = True
            
            if(last_price >= round(startPrice - points*7,5) and nine_7 == False and eight_active_7):
                blackSellLimit(0, black_volume_7, points*7, points*2, 7)
                nine_7 = True
        else :
            print("Sell Combination 7 failed")
            fail += 1
    #combination 8

if(succes):
    print("Succes")
else :
    print("Failed")

mt5.shutdown()