import MetaTrader5 as mt5
import time

mt5.initialize()

# startPrice < actual Price
symbol = "EURUSD"
startPrice = 1.07000
points = 0.0025

volume_1 = 0.16
volume_2 = 0.16
volume_3 = 0.16
black_volume_buyLimit_1 = 1.0
black_volume_SellLimit_1 = 0.4
black_volume_SellStop_2 = 0.4
black_volume_buyLimit_2 = 1.0
black_volume_SellStop_3 = 0.4
black_volume_buyLimit_3 = 1.0

blackbuyLimit_takeProfit_1 = points*3
blackbuyLimit_stopLoss_1 = points*2
blackSellLimit_takeProfit_1 = points*3
blackSellLimit_stopLoss_1 = points*2

blackbuyLimit_takeProfit_2 = points*3
blackbuyLimit_stopLoss_2 = points*2
blackSellStop_takeProfit_2 = points*2
blackSellStop_stopLoss_2 = points*3

blackbuyLimit_takeProfit_3 = points*3
blackbuyLimit_stopLoss_3 = points*2
blackSellStop_takeProfit_3 = points*3
blackSellStop_stopLoss_3 = points*2

failed_1 = False
failed_2 = False
failed_3 = False
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
    "comment":str(combination_number),
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
        print("Black SellLimit Order placement failed. Error code:", result.retcode)
    else:
        print("Black SellLimit order placed successfully. Order ticket:", result.order)

def blackSellStop(position, volume, st, tp, combination_number):
    order_type = mt5.ORDER_TYPE_SELL_STOP
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
        print("Black Sell Stop Order placement failed. Error code:", result.retcode)
    else:
        print("Black Sell Stop order placed successfully. Order ticket:", result.order)

def blackbuyLimit(position, volume, st, tp, combination_number):
    order_type = mt5.ORDER_TYPE_BUY_LIMIT       # Replace with the desired volume/lot size
    price = startPrice + position * points     # Set the price for the Buy Limit order
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
        print("Black Buy Limit Order placement failed. Error code:", result.retcode)
    else:
        print("Black Buy Limit order placed successfully. Order ticket:", result.order)

first_active_1 = False
second_active_1 = False
third_active_1 = False
fourd_active_1 = False
fifth_active_1 = False
sixth_active_1 = False

first_active_2 = False
second_active_2 = False
third_active_2 = False
fourd_active_2 = False
fifth_active_2 = False
sixth_active_2 = False

first_active_3 = False
second_active_3 = False
third_active_3 = False
fourd_active_3 = False
fifth_active_3 = False
sixth_active_3 = False

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

once = False

#insurance 1
buyLimit(0, volume_1, 1)

#insurance 2
buyLimit(0, volume_2, 2)

#insurance 3
buyLimit(0, volume_3, 3)

fail = 0
x = 0
last_price = startPrice
while fail != 3 and succes == False:

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
        first_active_1 = True
        first_active_2 = True
        first_active_3 = True
        sellLimit(1, volume_1*2, 1)
        buyStop(1, volume_2*2, 2)
        buyStop(1, volume_3*2, 3)
        once = True
    #insurance 1

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
            cancel_buyLimit_order(1)
        
        if(fourd_active_1 and last_price <= round(startPrice,5)):
            failed_1 = True
            fourd_active_1 = False
            cancel_SellLimit_order(1)

        if(fourd_active_1 and last_price >= round(startPrice + points*2,5)):
            fourd_active_1 = False
            fifth_active_1 = True
            cancel_SellLimit_order(1)

        if(fifth_active_1 and last_price >= round(startPrice + points*4,5)):
            failed_1 = True
            fifth_active_1 = False
            cancel_buyLimit_order(1)

        if(fifth_active_1 and last_price <= round(startPrice - points,5)):
            fifth_active_1 = False
            sixth_active_1 = True
            cancel_buyLimit_order(1)

        if(sixth_active_1 and last_price <= round(startPrice - points*3,5)):
            failed_1 = True
            sixth_active_1 = False

        if(sixth_active_1 and last_price >= round(startPrice + points*2,5)):
            sixth_active_1 = False
            print("Buy Insurance 1 finished")
            succes = True
            

        if(failed_1 == False):

            if(last_price >= round(startPrice + points,5) and third_1 == False and second_active_1):    
                buyLimit(0, volume_1*4, 1)
                third_1 = True

            if(last_price <= round(startPrice,5) and fourd_1 == False and third_active_1):
                buyStop(1, volume_1*8, 1)
                fourd_1 = True

            if(last_price >= round(startPrice + points,5) and fifth_1 == False and fourd_active_1):
                blackSellLimit(2, black_volume_SellLimit_1, blackSellLimit_stopLoss_1, blackSellLimit_takeProfit_1, 1)
                fifth_1 = True
            
            if(last_price >= round(startPrice + points*2,5) and sixth_1 == False and fifth_active_1):
                blackbuyLimit(-1,black_volume_buyLimit_1, blackbuyLimit_stopLoss_1, blackbuyLimit_takeProfit_1, 1)
                sixth_1 = True
        else :
            print("Insurance Buy 1 failed")
            fail += 1
        
    #insurance 2

    if(failed_2 == False):

        if(first_active_2 and last_price <= round(startPrice - points,5)):
            failed_2 = True
            first_active_2 = False
            cancel_buyStop_order(2)

        if(first_active_2 and last_price >= round(startPrice + points,5)):
            first_active_2 = False
            second_active_2 = True
            cancel_buyStop_order(2)

        if(second_active_2 and last_price <= round(startPrice,5)):
            failed_2 = True
            second_active_2 = False
            cancel_SellLimit_order(2)

        if(second_active_2 and last_price >= round(startPrice + points*2,5)):
            second_active_2 = False
            third_active_2 = True
            cancel_SellLimit_order(2)

        if(third_active_2 and last_price >= round(startPrice + points*3,5)):
            failed_2 = True
            third_active_2 = False
            cancel_SellStop_order(2)
        
        if(third_active_2 and last_price <= round(startPrice + points,5)):
            third_active_2 = False
            fourd_active_2 = True
            cancel_SellStop_order(2)
        
        if(fourd_active_2 and last_price >= round(startPrice+points*4,5)):
            failed_2 = True
            fourd_active_2 = False
            cancel_buyLimit_order(2)

        if(fourd_active_2 and last_price <= round(startPrice - points,5)):
            fourd_active_2 = False
            fifth_active_2 = True
            cancel_buyLimit_order(2)

        if(fifth_active_2 and last_price <= round(startPrice - points*3,5)):
            failed_2 = True
            fifth_active_2 = False

        if(fifth_active_2 and last_price >= round(startPrice + points*2,5)):
            fifth_active_2 = False
            print("Buy Insurance 2 finished")
            succes = True
            
        if(failed_2 == False):

            if(last_price >= round(startPrice + points,5) and third_2 == False and second_active_2):    
                sellLimit(2, volume_2*4, 2)
                third_2 = True

            if(last_price >= round(startPrice + points*2,5) and fourd_2 == False and third_active_2):
                blackSellStop(1, black_volume_SellStop_2, blackSellStop_stopLoss_2, blackSellStop_takeProfit_2, 2)
                fourd_2 = True

            if(last_price <= round(startPrice + points,5) and fifth_2 == False and fourd_active_2):
                blackbuyLimit(-1, black_volume_buyLimit_2, blackbuyLimit_stopLoss_2, blackbuyLimit_takeProfit_2, 2)
                fifth_2 = True
        else :
            print("Insurance Buy 2 failed")
            fail += 1
    
    #insurance 3

    if(failed_3 == False):
        
        if(first_active_3 and last_price <= round(startPrice - points,5)):
            failed_3 = True
            first_active_3 = False
            cancel_buyStop_order(3)

        if(first_active_3 and last_price >= round(startPrice + points,5)):
            first_active_3 = False
            second_active_3 = True
            cancel_buyStop_order(3)

        if(second_active_3 and last_price <= round(startPrice,5)):
            failed_3 = True
            second_active_3 = False
            cancel_buyStop_order(3)

        if(second_active_3 and last_price >= round(startPrice + points*2,5)):
            second_active_3 = False
            third_active_3 = True
            cancel_buyStop_order(3)

        if(third_active_3 and last_price <= round(startPrice + points,5)):
            failed_3 = True
            third_active_3 = False
            cancel_SellLimit_order(3)
        
        if(third_active_3 and last_price >= round(startPrice + points*3,5)):
            third_active_3 = False
            fourd_active_3 = True
            cancel_SellLimit_order(3)
        
        if(fourd_active_3 and last_price >= round(startPrice+points*4,5)):
            failed_3 = True
            fourd_active_3 = False
            cancel_SellStop_order(3)

        if(fourd_active_3 and last_price <= round(startPrice + points*2,5)):
            fourd_active_3 = False
            fifth_active_3 = True
            cancel_SellStop_order(3)


        if(fifth_active_3 and last_price >= round(startPrice + points*4,5)):
            failed_3 = True
            fifth_active_3 = False
            cancel_buyLimit_order(3)

        if(fifth_active_3 and last_price <= round(startPrice - points,5)):
            fifth_active_3 = False
            sixth_active_3 = True
            cancel_buyLimit_order(3)
        
        if(sixth_active_3 and last_price <= round(startPrice - points*3,5)):
            failed_3 = True
            sixth_active_3 = False

        if(sixth_active_3 and last_price >= round(startPrice + points*2,5)):
            sixth_active_3 = False
            print("Buy Insurance 3 finished")
            succes = True
        
            
        if(failed_3 == False):

            if(last_price >= round(startPrice + points,5) and third_3 == False and second_active_3):    
                buyStop(2, volume_3*4, 3)
                third_3 = True

            if(last_price >= round(startPrice + points*2,5) and fourd_3 == False and third_active_3):
                sellLimit(3, volume_3*8, 3)
                fourd_3 = True

            if(last_price >= round(startPrice + points*3,5) and fifth_3 == False and fourd_active_3):
                blackSellStop(2, black_volume_SellStop_3, blackSellStop_stopLoss_3, blackSellStop_takeProfit_3, 3)
                fifth_3 = True

            if(last_price <= round(startPrice + points*2,5) and sixth_3 == False and fifth_active_3):
                blackbuyLimit(-1, black_volume_buyLimit_3, blackbuyLimit_stopLoss_3, blackbuyLimit_takeProfit_3, 3)
                sixth_3 = True
        
        else :
            print("Insurance Buy 3 failed")
            fail += 1

if(succes):
    print("Buy Insurance finished")

else :
    print("Failed")
 
mt5.shutdown()