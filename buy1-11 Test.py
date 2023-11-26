import MetaTrader5 as mt5
import time

mt5.initialize()

#startPrice < actual Price

points = 0.0025
symbol = "EURUSD"
startPrice = 1.055

volume_1 = 0.07
volume_2 = 0.05
black_volume_2 = 0.85
volume_3 = 0.07
black_volume_3 = 0.85
volume_4 = 0.06
volume_5 = 0.06
black_volume_5 = 0.8
volume_6 = 0.05
black_volume_6 = 0.85
volume_7 = 0.05
black_volume_7 = 0.85
volume_8 = 0.04
black_volume_8 = 0.85
volume_9 = 0.05
black_volume_9 = 0.85
volume_10 = 0.04
black_volume_10 = 0.85
volume_11 = 0.05
black_volume_11 = 0.85


failed_1 = False
failed_2 = False
failed_3 = False
failed_4 = False
failed_5 = False
failed_6 = False
failed_7 = False
failed_8 = False
failed_9 = False
failed_10 = False
failed_11 = False

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
        print("Sell Stop order removed")

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
        print("Sell Limit order removed")

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
  
def blackSellLimit(position, volume, st, tp, combination_number):
    order_type = mt5.ORDER_TYPE_SELL_LIMIT
    price = startPrice + position * points
    stop_loss = price + st  # Replace with the desired stop loss price
    take_profit = price - tp  # Replace with the desired take profit price

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

def blackbuyLimit(position, volume, st, tp, combination_number):
    order_type = mt5.ORDER_TYPE_BUY_LIMIT       # Replace with the desired volume/lot size
    price = startPrice - position * points     # Set the price for the Buy Limit order
    stop_loss = price - st  # Replace with the desired stop loss price
    take_profit = price + tp  # Replace with the desired take profit price
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
        print("Black BuyLimit Order placement failed. Error code:", result.retcode)
    else:
        print("Black BuyLimit order placed successfully. Order ticket:", result.order)


first_active_1 = False
second_active_1 = False
third_active_1  = False
fourd_active_1  = False
fifth_active_1  = False
sixth_active_1  = False

first_active_2 = False
second_active_2 = False
third_active_2 = False
fourd_active_2 = False
fifth_active_2 = False
sixth_active_2 = False

first_active_3 = False
second_active_3 = False
third_active_3  = False
fourd_active_3  = False
fifth_active_3  = False
sixth_active_3  = False

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

first_active_6 = False
second_active_6 = False
third_active_6 = False
fourd_active_6 = False
fifth_active_6 = False
sixth_active_6 = False

first_active_7 = False
second_active_7 = False
third_active_7 = False
fourd_active_7 = False
fifth_active_7 = False
sixth_active_7 = False
seventh_active_7 = False

first_active_8 = False
second_active_8 = False
third_active_8 = False
fourd_active_8 = False
fifth_active_8 = False
sixth_active_8 = False
seventh_active_8 = False

first_active_9 = False
second_active_9 = False
third_active_9 = False
fourd_active_9 = False
fifth_active_9 = False

first_active_10 = False
second_active_10 = False
third_active_10 = False
fourd_active_10 = False
fifth_active_10 = False
sixth_active_10 = False
seventh_active_10 = False

first_active_11 = False
second_active_11 = False
third_active_11 = False
fourd_active_11 = False
fifth_active_11 = False
sixth_active_11 = False

third_1 = False
fourd_1 = False
fifth_1 = False
sixth_1 = False

third_2 = False
fourd_2 = False
fifth_2 = False
sixth_2 = False

third_3 = False
fourd_3 = False
fifth_3 = False
sixth_3 = False

third_4 = False
fourd_4 = False
fifth_4 = False
sixth_4 = False

third_5 = False
fourd_5 = False
fifth_5 = False
sixth_5 = False

third_6 = False
fourd_6 = False
fifth_6 = False
sixth_6 = False

third_7 = False
fourd_7 = False
fifth_7 = False
sixth_7 = False
seven_7 = False

third_8 = False
fourd_8 = False
fifth_8 = False
sixth_8 = False
seven_8 = False

third_9 = False
fourd_9 = False
fifth_9 = False

third_10 = False
fourd_10 = False
fifth_10 = False
sixth_10 = False
seven_10 = False

third_11 = False
fourd_11 = False
fifth_11 = False
sixth_11 = False

once = False

print("Buy1-11 Start")
#combination 1
buyLimit(0, volume_1, 1)

#combination 2
buyLimit(0, volume_2, 2)

#combination 3
buyLimit(0, volume_3, 3)

#combination 4
buyLimit(0, volume_4, 4)

#combination 5
buyLimit(0, volume_5, 5)

#combination 6
buyLimit(0, volume_6, 6)

#combination 7
buyLimit(0, volume_7, 7)

#combination 8
buyLimit(0, volume_8, 8)

#combination 9
buyLimit(0, volume_9, 9)

#combination 10
buyLimit(0, volume_10, 10)

#combination 11
buyLimit(0, volume_11, 11)

fail = 0
x = 0
last_price = startPrice
while fail != 11 and succes == False:


    if(x == 1):
        last_price += points
        last_price = round(last_price, 5)
        print("2")
    if(x == 2):
        last_price -= points
        last_price = round(last_price, 5)
        print("3")
    '''if(x == 3):
        last_price += points
        last_price = round(last_price, 5)
        print("4")
    if(x == 4):
        last_price += points
        last_price = round(last_price, 5)
        print("5")
    if(x == 5):
        last_price += points
        last_price = round(last_price, 5)
        print("6")
    if(x == 6):
        last_price -= points
        last_price = round(last_price, 5)
        print("7")
    if(x == 7):
        last_price += points*2
        last_price = round(last_price, 5)'''
    

    x += 1

    #last_price = mt5.symbol_info_tick(symbol).ask
         
    if(last_price <= startPrice and once == False):

        first_active_1 = True
        first_active_2 = True
        first_active_3 = True
        first_active_4 = True
        first_active_5 = True
        first_active_6 = True
        first_active_7 = True
        first_active_8 = True
        first_active_9 = True
        first_active_10 = True
        first_active_11 = True
        sellLimit(-1, volume_1*2, 1)
        sellLimit(-1, volume_2*2, 2)
        sellLimit(-1, volume_3*2, 3)
        buyStop(1, volume_4*2, 4)
        buyStop(1, volume_5*2, 5)
        buyStop(1, volume_6*2, 6)
        sellLimit(-1, volume_7*2, 7)
        buyStop(1, volume_8*2, 8)
        buyStop(1, volume_9*2, 9)
        buyStop(1, volume_10*2, 10)
        buyStop(1, volume_11*2, 11)
        cancel_buyLimit_order(1)
        cancel_buyLimit_order(2)
        cancel_buyLimit_order(3)
        cancel_buyLimit_order(4)
        cancel_buyLimit_order(5)
        cancel_buyLimit_order(6)
        cancel_buyLimit_order(7)
        cancel_buyLimit_order(8)
        cancel_buyLimit_order(9)
        cancel_buyLimit_order(10)
        cancel_buyLimit_order(11)
        once = True
    #combination 1

    if(failed_1 == False):
        
        if(first_active_1 and last_price <= round(startPrice - points,5)):
            failed_1 = True
            first_active_1 = False
            cancel_SellLimit_order(1)

        if(first_active_1 and last_price >= round(startPrice + points,5)):
            first_active_1 = False
            second_active_1 = True
            cancel_SellLimit_order(1)

        if(second_active_1 and last_price >= round(startPrice + points*2,5)):
            failed_1 = True
            second_active_1 = False
            cancel_buyLimit_order(1)

        if(second_active_1 and last_price <= round(startPrice,5)):
            second_active_1 = False
            third_active_1 = True
            cancel_buyLimit_order(1)

        if(third_active_1 and last_price <= round(startPrice - points,5)):
            failed_1 = True
            third_active_1 = False
            cancel_buyStop_order(1)
        
        if(third_active_1 and last_price >= round(startPrice + points,5)):
            third_active_1 = False
            fourd_active_1 = True
            cancel_buyStop_order(1)
        
        if(fourd_active_1 and last_price <= round(startPrice,5)):
            failed_1 = True
            fourd_active_1 = False
            cancel_buyStop_order(1)

        if(fourd_active_1 and last_price >= round(startPrice + points*2,5)):
            fourd_active_1 = False
            fifth_active_1 = True
            cancel_buyStop_order(1)

        if(fifth_active_1 and last_price <= round(startPrice + points,5)):
            failed_1 = True
            fifth_active_1 = False
            cancel_buyStop_order(1)

        if(fifth_active_1 and last_price >= round(startPrice + points*3,5)):
            fifth_active_1 = False
            sixth_active_1 = True
            cancel_buyStop_order(1)
        
        if(sixth_active_1 and last_price <= round(startPrice + points*2,5)):
            failed_1 = True    
            sixth_active_1 = False

        if(sixth_active_1 and last_price >= round(startPrice + points*4,5)):            
            print("Buy Combination 1 finished")
            succes = True

        if(failed_1 == False):

            if(last_price >= round(startPrice + points,5) and third_1 == False and second_active_1):    
                buyLimit(0, volume_1*4, 1)
                third_1 = True

            if(last_price <= round(startPrice,5) and fourd_1 == False and third_active_1):
                buyStop(1, volume_1*8, 1)
                fourd_1 = True
            
            if(last_price >= round(startPrice + points,5) and fifth_1 == False and fourd_active_1):
                buyStop(2, volume_1*16, 1)
                fifth_1 = True
            
            if(last_price >= round(startPrice + points * 2,5) and sixth_1 == False and fifth_active_1):
                buyStop(3, volume_1*32, 1)
                sixth_1 = True
        else :
            print("Buy Combination 1 failed")
            fail += 1
    
    #combination 2

    if(failed_2 == False):

        if(first_active_2 and last_price <= round(startPrice - points,5)):
            failed_2 = True
            first_active_2 = False
            cancel_SellLimit_order(2)

        if(first_active_2 and last_price >= round(startPrice + points,5)):
            first_active_2 = False
            second_active_2 = True
            cancel_SellLimit_order(2)

        if(second_active_2 and last_price >= round(startPrice + points*2,5)):
            failed_2 = True
            second_active_2 = False
            cancel_buyLimit_order(2)

        if(second_active_2 and last_price <= round(startPrice,5)):
            second_active_2 = False
            third_active_2 = True
            cancel_buyLimit_order(2)

        if(third_active_2 and last_price <= round(startPrice - points,5)):
            failed_2 = True
            third_active_2 = False
            cancel_SellLimit_order(2)
        
        if(third_active_2 and last_price >= round(startPrice + points,5)):
            third_active_2 = False
            fourd_active_2 = True
            cancel_SellLimit_order(2)
        
        if(fourd_active_2 and last_price >= round(startPrice + points*2,5)):
            failed_2 = True
            fourd_active_2 = False
            cancel_buyLimit_order(2)

        if(fourd_active_2 and last_price <= round(startPrice,5)):
            fourd_active_2 = False
            fifth_active_2 = True
            cancel_buyLimit_order(2)

        if(fifth_active_2 and last_price <= round(startPrice - points,5)):
            failed_2 = True
            fifth_active_2 = False

        if(fifth_active_2 and last_price >= round(startPrice + points*4,5)):
            fifth_active_2 = False
            print("Buy Combination 2 finished")
            succes = True

        if(failed_2 == False):

            if(last_price >= round(startPrice + points,5) and third_2 == False and second_active_2):    
                buyLimit(0, volume_2*4,2)
                third_2 = True

            if(last_price <= round(startPrice,5) and fourd_2 == False and third_active_2):
                sellLimit(-1, volume_2*8, 2)
                fourd_2 = True
            
            if(last_price >= round(startPrice + points,5) and fifth_2 == False and fourd_active_2):
                blackbuyLimit(0, black_volume_2,points*1, points*4, 2)
                fifth_2 = True
        else :
            print("Buy Combination 2 failed")
            fail += 1
    #combination 3

    if(failed_3 == False):

        if(first_active_3 and last_price <= round(startPrice - points,5)):
            failed_3 = True
            first_active_3 = False
            cancel_SellLimit_order(3)

        if(first_active_3 and last_price >= round(startPrice + points,5)):
            first_active_3 = False
            second_active_3 = True
            cancel_SellLimit_order(3)

        if(second_active_3 and last_price >= round(startPrice + points*2,5)):
            failed_3 = True
            second_active_3 = False
            cancel_buyLimit_order(3)

        if(second_active_3 and last_price <= round(startPrice,5)):
            second_active_3 = False
            third_active_3 = True
            cancel_buyLimit_order(3)

        if(third_active_3 and last_price <= round(startPrice - points,5)):
            failed_3 = True
            third_active_3 = False
            cancel_buyStop_order(3)
        
        if(third_active_3 and last_price >= round(startPrice + points,5)):
            third_active_3 = False
            fourd_active_3 = True
            cancel_buyStop_order(3)
        
        if(fourd_active_3 and last_price <= round(startPrice,5)):
            failed_3 = True
            fourd_active_3 = False
            cancel_SellLimit_order(3)

        if(fourd_active_3 and last_price >= round(startPrice + points*2,5)):
            fourd_active_3 = False
            fifth_active_3 = True
            cancel_SellLimit_order(3)

        if(fifth_active_3 and last_price >= round(startPrice + points*3,5)):
            failed_3 = True
            fifth_active_3 = False
            cancel_buyLimit_order(3)

        if(fifth_active_3 and last_price <= round(startPrice + points,5)):
            fifth_active_3 = False
            sixth_active_3 = True
            cancel_buyLimit_order(3)

        if(sixth_active_3 and last_price <= round(startPrice - points,5)):
            failed_3 = True
            sixth_active_3 = False
        
        if(sixth_active_3 and last_price >= round(startPrice + points*4,5)):
            sixth_active_3 = False
            print("Buy Combination 3 finished")
            succes = True
            

        if(failed_3 == False):

            if(last_price >= round(startPrice + points,5) and third_3 == False and second_active_3):    
                buyLimit(0, volume_3*4, 3)
                third_3 = True

            if(last_price <= round(startPrice,5) and fourd_3 == False and third_active_3):
                buyStop(1, volume_3*8, 3)
                fourd_3 = True
            
            if(last_price >= round(startPrice + points,5) and fifth_3 == False and fourd_active_3):
                sellLimit(-2, volume_3*16, 3)
                fifth_3 = True
            
            if(last_price >= round(startPrice + points * 2,5) and sixth_3 == False and fifth_active_3):
                blackbuyLimit(1, black_volume_3, points*2, points*3, 3)
                sixth_3 = True
        else :
            print("Buy Combination 3 failed")
            fail += 1

    #combination 4

    if(failed_4 == False):

        if(first_active_4 and last_price <= round(startPrice - points,5)):
            failed_4 = True
            first_active_4 = False
            cancel_buyStop_order(4)

        if(first_active_4 and last_price >= round(startPrice + points,5)):
            first_active_4 = False
            second_active_4 = True
            cancel_buyStop_order(4)

        if(second_active_4 and last_price <= round(startPrice,5)):
            failed_4 = True
            second_active_4 = False
            cancel_SellLimit_order(4)

        if(second_active_4 and last_price >= round(startPrice + points*2,5)):
            second_active_4 = False
            third_active_4 = True
            cancel_SellLimit_order(4)

        if(third_active_4 and last_price >= round(startPrice + points*3,5)):       
            failed_4 = True
            third_active_4 = False
            cancel_buyLimit_order(4)
        
        if(third_active_4 and last_price <= round(startPrice + points,5)):
            third_active_4 = False    
            fourd_active_4 = True
            cancel_buyLimit_order(4)
        
        if(fourd_active_4 and last_price <= round(startPrice,5)):
            failed_4 = True
            fourd_active_4 = False
            cancel_buyStop_order(4)

        if(fourd_active_4 and last_price >= round(startPrice + points*2,5)):
            fourd_active_4 = False
            fifth_active_4 = True
            cancel_buyStop_order(4)
        
        if(fifth_active_4 and last_price <= round(startPrice + points,5)):
            failed_4 = True
            fifth_active_4 = False
            cancel_buyStop_order(4)

        if(fifth_active_4 and last_price >= round(startPrice + points*3,5)):
            fifth_active_4 = False
            sixth_active_4 = True
            cancel_buyStop_order(4)
        
        if(sixth_active_4 and last_price <= round(startPrice + points*2,5)):
            failed_4 = True
            sixth_active_4 = False
        
        if(sixth_active_4 and last_price >= round(startPrice + points*4,5)):
            sixth_active_4 = False
            print("Buy Combination 4 finished")
            succes = True

        if(failed_4 == False):

            if(last_price >= round(startPrice + points,5) and third_4 == False and second_active_4):    
                sellLimit(-2, volume_4*4, 4)
                third_4 = True

            if(last_price >= round(startPrice + points * 2,5) and fourd_4 == False and third_active_4):
                buyLimit(1, volume_4*8, 4)
                fourd_4 = True
            
            if(last_price <= round(startPrice + points,5) and fifth_4 == False and fourd_active_4):
                buyStop(2, volume_4*16, 4)
                fifth_4 = True
            
            if(last_price >= round(startPrice + points * 2,5) and sixth_4 == False and fifth_active_4):
                buyStop(3, volume_4*32, 4)
                sixth_4 = True
        else :
            print("Buy Combination 4 failed")
            fail += 1
    #combination 5

    if(failed_5 == False):

        if(first_active_5 and last_price <= round(startPrice - points,5)):
            failed_5 = True
            first_active_5 = False
            cancel_buyStop_order(5)

        if(first_active_5 and last_price >= round(startPrice + points,5)):
            first_active_5 = False
            second_active_5 = True
            cancel_buyStop_order(5)

        if(second_active_5 and last_price <= round(startPrice,5)):
            failed_5 = True
            second_active_5 = False
            cancel_buyStop_order(5)

        if(second_active_5 and last_price >= round(startPrice + points*2,5)):
            second_active_5 = False
            third_active_5 = True
            cancel_buyStop_order(5)

        if(third_active_5 and last_price <= round(startPrice + points,5)):       
            failed_5 = True
            third_active_5 = False
            cancel_SellLimit_order(5)
        
        if(third_active_5 and last_price >= round(startPrice + points*3,5)):
            third_active_5 = False    
            fourd_active_5 = True
            cancel_SellLimit_order(5)
        
        if(fourd_active_5 and last_price >= round(startPrice + points*4,5)):
            failed_5 = True
            fourd_active_5 = False
            cancel_buyLimit_order(5)

        if(fourd_active_5 and last_price <= round(startPrice +points*2,5)):
            fourd_active_5 = False
            fifth_active_5 = True
            cancel_buyLimit_order(5)
        
        if(fifth_active_5 and last_price <= round(startPrice + points,5)):
            failed_5 = True
            fifth_active_5 = False
            cancel_buyStop_order(5)

        if(fifth_active_5 and last_price >= round(startPrice + points*3,5)):
            fifth_active_5 = False
            sixth_active_5 = True
            cancel_buyStop_order(5)
        
        if(sixth_active_5 and last_price <= round(startPrice + points*2,5)):
            failed_5 = True
            sixth_active_5 = False
        
        if(sixth_active_5 and last_price >= round(startPrice + points*4,5)):
            sixth_active_5 = False
            print("Buy Combination 5 finished")
            succes = True

        if(failed_5 == False):

            if(last_price >= round(startPrice + points,5) and third_5 == False and second_active_5):    
                buyStop(2, volume_5*4, 5)
                third_5 = True

            if(last_price >= round(startPrice + points * 2,5) and fourd_5 == False and third_active_5):
                sellLimit(-3, volume_5*8, 5)
                fourd_5 = True
            
            if(last_price >= round(startPrice + points * 3,5) and fifth_5 == False and fourd_active_5):
                buyLimit(2, volume_5*16, 5)
                fifth_5 = True
            
            if(last_price <= round(startPrice + points * 2,5) and sixth_5 == False and fifth_active_5):
                buyStop(3, volume_5*32, 5)
                sixth_5 = True
        else :
            print("Buy Combination 5 failed")
            fail += 1
    #combination 6

    if(failed_6 == False):

        if(first_active_6 and last_price <= round(startPrice - points,5)):
            failed_6 = True
            first_active_6 = False
            cancel_buyStop_order(6)

        if(first_active_6 and last_price >= round(startPrice + points,5)):
            first_active_6 = False
            second_active_6 = True
            cancel_buyStop_order(6)

        if(second_active_6 and last_price <= round(startPrice,5)):
            failed_6 = True
            second_active_6 = False
            cancel_SellLimit_order(6)

        if(second_active_6 and last_price >= round(startPrice + points*2,5)):
            second_active_6 = False
            third_active_6 = True
            cancel_SellLimit_order(6)

        if(third_active_6 and last_price >= round(startPrice + points *3,5)):
            failed_6 = True
            third_active_6 = False
            cancel_buyLimit_order(6)
        
        if(third_active_6 and last_price <= round(startPrice + points,5)):
            third_active_6 = False
            fourd_active_6 = True
            cancel_buyLimit_order(6)
        
        if(fourd_active_6 and last_price <= round(startPrice,5)):
            failed_6 = True
            fourd_active_6 = False
            cancel_SellLimit_order(6)

        if(fourd_active_6 and last_price >= round(startPrice + points*2,5)):
            fourd_active_6 = False
            fifth_active_6 = True
            cancel_SellLimit_order(6)

        if(fifth_active_6 and last_price >= round(startPrice + points*3,5)):
            failed_6 = True
            fifth_active_6 = False
            cancel_buyLimit_order(6)

        if(fifth_active_6 and last_price <= round(startPrice + points,5)):
            fifth_active_6 = False
            sixth_active_6 = True
            cancel_buyLimit_order(6)

        if(sixth_active_6 and last_price <= round(startPrice - points,5)):
            failed_6 = True
            sixth_active_6 = False
        
        if(sixth_active_6 and last_price >= round(startPrice + points*4,5)):
            sixth_active_6 = False
            print("Buy Combination 6 finished")
            succes = True

        if(failed_6 == False):

            if(last_price >= round(startPrice + points,5) and third_6 == False and second_active_6):    
                sellLimit(-2, volume_6*4, 6)
                third_6 = True

            if(last_price >= round(startPrice + points * 2,5) and fourd_6 == False and third_active_6):
                buyLimit(1, volume_6*8, 6)
                fourd_6 = True
            
            if(last_price <= round(startPrice + points,5) and fifth_6 == False and fourd_active_6):
                sellLimit(-2, volume_6*16, 6)
                fifth_6 = True
            
            if(last_price >= round(startPrice + points * 2,5) and sixth_6 == False and fifth_active_6):
                blackbuyLimit(1, black_volume_6, points*2, points*3, 6)
                sixth_6 = True
        else :
            print("Buy Combination 6 failed")
            fail += 1
    #combination 7

    if(failed_7 == False):

        if(first_active_7 and last_price <= round(startPrice - points,5)):
            failed_7 = True
            first_active_7 = False
            cancel_SellLimit_order(7)

        if(first_active_7 and last_price >= round(startPrice + points,5)):
            first_active_7 = False
            second_active_7 = True
            cancel_SellLimit_order(7)

        if(second_active_7 and last_price >= round(startPrice + points*2,5)):
            failed_7 = True
            second_active_7 = False
            cancel_buyLimit_order(7)

        if(second_active_7 and last_price <= round(startPrice,5)):
            second_active_7 = False
            third_active_7 = True
            cancel_buyLimit_order(7)

        if(third_active_7 and last_price <= round(startPrice - points,5)):
            failed_7 = True
            third_active_7 = False
            cancel_buyStop_order(7)
        
        if(third_active_7 and last_price >= round(startPrice + points,5)):
            third_active_7 = False
            fourd_active_7 = True
            cancel_buyStop_order(7)
        
        if(fourd_active_7 and last_price <= round(startPrice,5)):
            failed_7 = True
            fourd_active_7 = False
            cancel_buyStop_order(7)

        if(fourd_active_7 and last_price >= round(startPrice + points*2,5)):
            fourd_active_7 = False
            fifth_active_7 = True
            cancel_buyStop_order(7)

        if(fifth_active_7 and last_price <= round(startPrice + points,5)):
            failed_7 = True
            fifth_active_7 = False
            cancel_SellLimit_order(7)

        if(fifth_active_7 and last_price >= round(startPrice + points*3,5)):
            fifth_active_7 = False
            sixth_active_7 = True
            cancel_SellLimit_order(7)

        if(sixth_active_7 and last_price >= round(startPrice + points*4,5)):
            failed_7 = True
            sixth_active_7 = False
            cancel_buyLimit_order(7)
        
        if(sixth_active_7 and last_price <= round(startPrice + points*2,5)):
            sixth_active_7 = False
            seventh_active_7 = True
            cancel_buyLimit_order(7)

        if(seventh_active_7 and last_price <= round(startPrice - points,5)):
            failed_7 = True
            seventh_active_7 = False
        
        if(seventh_active_7 and last_price >= round(startPrice + points*4,5)):
            seventh_active_7 = False
            print("Buy Combination 7 finished")
            succes = True
            

        if(failed_7 == False):

            if(last_price >= round(startPrice + points,5) and third_7 == False and second_active_7):    
                buyLimit(0, volume_7*4,7)
                third_7 = True

            if(last_price <= round(startPrice,5) and fourd_7 == False and third_active_7):
                buyStop(1, volume_7*8, 7)
                fourd_7 = True
            
            if(last_price >= round(startPrice + points,5) and fifth_7 == False and fourd_active_7):
                buyStop(2, volume_7*16, 7)
                fifth_7 = True
            
            if(last_price >= round(startPrice + points * 2,5) and sixth_7 == False and fifth_active_7):
                sellLimit(-3, volume_7*32, 7)
                sixth_7 = True

            if(last_price >= round(startPrice + points * 3,5) and seven_7 == False and sixth_active_7):
                blackbuyLimit(2, black_volume_7, points*3, points*2, 7)
                seven_7 = True
        else :
            print("Buy Combination 7 failed")
            fail += 1
    #combination 8

    if(failed_8 == False):

        if(first_active_8 and last_price <= round(startPrice - points,5)):
            failed_8 = True
            first_active_8 = False
            cancel_buyStop_order(8)

        if(first_active_8 and last_price >= round(startPrice + points,5)):
            first_active_8 = False
            second_active_8 = True
            cancel_buyStop_order(8)

        if(second_active_8 and last_price <= round(startPrice,5)):
            failed_8 = True
            second_active_8 = False
            cancel_SellLimit_order(8)

        if(second_active_8 and last_price >= round(startPrice + points*2,5)):
            second_active_8 = False
            third_active_8 = True
            cancel_SellLimit_order(8)

        if(third_active_8 and last_price >= round(startPrice + points *3,5)):
            failed_8 = True
            third_active_8 = False
            cancel_buyLimit_order(8)
        
        if(third_active_8 and last_price <= round(startPrice + points,5)):
            third_active_8 = False
            fourd_active_8 = True
            cancel_buyLimit_order(8)
        
        if(fourd_active_8 and last_price <= round(startPrice,5)):
            failed_8 = True
            fourd_active_8 = False
            cancel_buyStop_order(8)

        if(fourd_active_8 and last_price >= round(startPrice + points*2,5)):
            fourd_active_8 = False
            fifth_active_8 = True
            cancel_buyStop_order(8)

        if(fifth_active_8 and last_price <= round(startPrice + points,5)):
            failed_8 = True
            fifth_active_8 = False
            cancel_SellLimit_order(8)

        if(fifth_active_8 and last_price >= round(startPrice + points*3,5)):
            fifth_active_8 = False
            sixth_active_8 = True
            cancel_SellLimit_order(8)

        if(sixth_active_8 and last_price >= round(startPrice + points*4,5)):
            failed_8 = True
            sixth_active_8 = False
            cancel_buyLimit_order(8)
        
        if(sixth_active_8 and last_price <= round(startPrice + points*2,5)):
            sixth_active_8 = False
            seventh_active_8 = True
            cancel_buyLimit_order(8)

        if(seventh_active_8 and last_price <= round(startPrice - points,5)):
            failed_8 = True
            seventh_active_8 = False
        
        if(seventh_active_8 and last_price >= round(startPrice + points*4,5)):
            seventh_active_8 = False
            print("Buy Combination 8 finished")
            succes = True

        if(failed_8 == False):

            if(last_price >= round(startPrice + points,5) and third_8 == False and second_active_8):    
                sellLimit(-2, volume_8*4, 8)
                third_8 = True

            if(last_price >= round(startPrice + points*2,5) and fourd_8 == False and third_active_8):
                buyLimit(1, volume_8*8, 8)
                fourd_8 = True
            
            if(last_price <= round(startPrice + points,5) and fifth_8 == False and fourd_active_8):
                buyStop(2, volume_8*16, 8)
                fifth_8 = True
            
            if(last_price >= round(startPrice + points * 2,5) and sixth_8 == False and fifth_active_8):
                sellLimit(-3, volume_8*32, 8)
                sixth_8 = True

            if(last_price >= round(startPrice + points * 3,5) and seven_8 == False and sixth_active_8):
                blackbuyLimit(2, black_volume_8, points*3, points*2, 8)
                seven_8 = True
        else :
            print("Buy Combination 8 failed")
            fail += 1
    #combination 9

    if(failed_9 == False):
        
        if(first_active_9 and last_price <= round(startPrice - points,5)):
            failed_9 = True
            first_active_9 = False
            cancel_buyStop_order(9)

        if(first_active_9 and last_price >= round(startPrice + points,5)):
            first_active_9 = False
            second_active_9 = True
            cancel_buyStop_order(9)

        if(second_active_9 and last_price <= round(startPrice,5)):
            failed_9 = True
            second_active_9 = False
            cancel_SellLimit_order(9)

        if(second_active_9 and last_price >= round(startPrice + points*2,5)):
            second_active_9 = False
            third_active_9 = True
            cancel_SellLimit_order(9)

        if(third_active_9 and last_price >= round(startPrice + points *3,5)):
            failed_9 = True
            third_active_9 = False
            cancel_SellStop_order(9)
        
        if(third_active_9 and last_price <= round(startPrice + points,5)):
            third_active_9 = False
            fourd_active_9 = True
            cancel_SellStop_order(9)
        
        if(fourd_active_9 and last_price >= round(startPrice + points*2,5)):
            failed_9 = True
            fourd_active_9  = False
            cancel_buyLimit_order(9)

        if(fourd_active_9 and last_price <= round(startPrice,5)):
            fourd_active_9 = False
            fifth_active_9 = True
            cancel_buyLimit_order(9)

        if(fifth_active_9 and last_price <= round(startPrice - points,5)):
            failed_9 = True
            fifth_active_9 = False

        if(fifth_active_9 and last_price >= round(startPrice + points*4,5)):
            fifth_active_9 = False
            print("Buy Combination 9 finished")
            succes = True

        if(failed_9 == False):

            if(last_price >= round(startPrice + points,5) and third_9 == False and second_active_9):    
                sellLimit(-2, volume_9*4, 9)
                third_9 = True

            if(last_price >= round(startPrice + points * 2,5) and fourd_9 == False and third_active_9):
                sellStop(1, volume_9*8, 9)
                fourd_9 = True
            
            if(last_price <= round(startPrice + points,5) and fifth_9 == False and fourd_active_9):
                blackbuyLimit(0, black_volume_9, points*1, points*4, 9)
                fifth_9 = True   
        else :
            print("Buy Combination 9 failed")
            fail += 1
    #combination 10

    if(failed_10 == False):
        
        if(first_active_10 and last_price <= round(startPrice - points,5)):
            failed_10 = True
            first_active_10 = False
            cancel_buyStop_order(10)

        if(first_active_10 and last_price >= round(startPrice + points,5)):
            first_active_10 = False
            second_active_10 = True
            cancel_buyStop_order(10)

        if(second_active_10 and last_price <= round(startPrice,5)):
            failed_10 = True
            second_active_10 = False
            cancel_buyStop_order(10)

        if(second_active_10 and last_price >= round(startPrice + points*2,5)):
            second_active_10 = False
            third_active_10 = True
            cancel_buyStop_order(10)

        if(third_active_10 and last_price <= round(startPrice + points,5)):       
            failed_10 = True
            third_active_10 = False
            cancel_SellLimit_order(10)
        
        if(third_active_10 and last_price >= round(startPrice + points*3,5)):
            third_active_10 = False    
            fourd_active_10 = True
            cancel_SellLimit_order(10)
        
        if(fourd_active_10 and last_price >= round(startPrice + points*4,5)):
            failed_10 = True
            fourd_active_10 = False
            cancel_buyLimit_order(10)

        if(fourd_active_10 and last_price <= round(startPrice +points*2,5)):
            fourd_active_10 = False
            fifth_active_10 = True
            cancel_buyLimit_order(10)
        
        if(fifth_active_10 and last_price <= round(startPrice + points,5)):
            failed_10 = True
            fifth_active_10 = False
            cancel_SellLimit_order(10)

        if(fifth_active_10 and last_price >= round(startPrice + points*3,5)):
            fifth_active_10 = False
            sixth_active_10 = True
            cancel_SellLimit_order(10)
        
        if(sixth_active_10 and last_price >= round(startPrice + points*4,5)):
            failed_10 = True
            sixth_active_10 = False
            cancel_buyLimit_order(10)
        
        if(sixth_active_10 and last_price <= round(startPrice + points*2,5)):
            sixth_active_10 = False
            seventh_active_10 = True
            cancel_buyLimit_order(10)

        if(seventh_active_10 and last_price <= round(startPrice - points,5)):
            failed_10 = True
            seventh_active_10 = False
        
        if(seventh_active_10 and last_price >= round(startPrice + points*4,5)):
            seventh_active_10 = False
            print("Buy Combination 10 finished")
            succes = True

        if(failed_10 == False):

            if(last_price >= round(startPrice + points,5) and third_10 == False and second_active_10):    
                buyStop(2, volume_10*4, 10)
                third_10 = True

            if(last_price >= round(startPrice + points * 2,5) and fourd_10 == False and third_active_10):
                sellLimit(-3, volume_10*8, 10)
                fourd_10 = True
            
            if(last_price >= round(startPrice + points * 3,5) and fifth_10 == False and fourd_active_10):
                buyLimit(2, volume_10*16, 10)
                fifth_10 = True
            
            if(last_price <= round(startPrice + points * 2,5) and sixth_10 == False and fifth_active_10):
                sellLimit(-3, volume_10*32, 10)
                sixth_10 = True
            
            if(last_price >= round(startPrice + points * 3,5) and seven_10 == False and sixth_active_10):
                blackbuyLimit(2, black_volume_10, points*3, points*2, 10)
                seven_10 = True  
            
        else :
            print("Buy Combination 10 failed")
            fail += 1
    #combination 11

    if(failed_11 == False):

        if(first_active_11 and last_price <= round(startPrice - points,5)):
            failed_11 = True
            first_active_11 = False
            cancel_buyStop_order(11)

        if(first_active_11 and last_price >= round(startPrice + points,5)):
            first_active_11 = False
            second_active_11 = True
            cancel_buyStop_order(11)

        if(second_active_11 and last_price <= round(startPrice,5)):
            failed_11 = True
            second_active_11 = False
            cancel_buyStop_order(11)

        if(second_active_11 and last_price >= round(startPrice + points*2,5)):
            second_active_11 = False
            third_active_11 = True
            cancel_buyStop_order(11)

        if(third_active_11 and last_price <= round(startPrice + points,5)):       
            failed_11 = True
            third_active_11 = False
            cancel_SellLimit_order(11)
        
        if(third_active_11 and last_price >= round(startPrice + points*3,5)):
            third_active_11 = False    
            fourd_active_11 = True
            cancel_SellLimit_order(11)
        
        if(fourd_active_11 and last_price >= round(startPrice + points*4,5)):
            failed_11 = True
            fourd_active_11 = False
            cancel_SellStop_order(11)
    
        if(fourd_active_11 and last_price <= round(startPrice + points*2,5)):
            fourd_active_11 = False
            fifth_active_11 = True
            cancel_SellStop_order(11)
        
        if(fifth_active_11 and last_price >= round(startPrice + points*3,5)):
            failed_11 = True
            fifth_active_11 = False
            cancel_buyLimit_order(11)

        if(fifth_active_11 and last_price <= round(startPrice + points,5)):
            fifth_active_11 = False
            sixth_active_11 = True
            cancel_buyLimit_order(11)
        
        if(sixth_active_11 and last_price <= round(startPrice - points,5)):
            failed_11 = True
            sixth_active_11 = False
            
        if(sixth_active_11 and last_price >= round(startPrice + points*4,5)):
            sixth_active_11 = False
            print("Buy Combination 11 finished")
            succes = True


        if(failed_11 == False):

            if(last_price >= round(startPrice + points,5) and third_11 == False and second_active_11):    
                buyStop(2, volume_11*4, 11)
                third_11 = True

            if(last_price >= round(startPrice + points * 2,5) and fourd_11 == False and third_active_11):
                sellLimit(-3, volume_11*8, 11)
                fourd_11 = True
            
            if(last_price >= round(startPrice + points * 3,5) and fifth_11 == False and fourd_active_11):
                sellStop(2, volume_11*16, 11)
                fifth_11 = True
            
            if(last_price <= round(startPrice + points * 2,5) and sixth_11 == False and fifth_active_11):
                blackbuyLimit(1, black_volume_11, points*2, points*3, 11)
                sixth_11 = True
        else :
            print("Buy Combination 11 failed")
            fail += 1
if(succes):
    print("succes")

else :
    print("Fail")

mt5.shutdown()