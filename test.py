import time

startPrice = 1.0
last_price = 1.0
volume = 0.6
points = 0.25

failed = False
succes = False

def cancel_buyLimit_order(combination_number, step):
    print("Cancel buyLimit Order")

def cancel_buyStop_order(combination_number, step):
    print("Cancel buyStop Order")

def cancel_SellStop_order(combination_number, step):
    print("Cancel SellStop Order")

def cancel_SellLimit_order(combination_number, step):
    print("Cancel SellLimit Order")

def buyLimit():
    
    print("Buy Limit order placed successfully. Order ticket:")

def sellStop():
    
    print("Sell Stop order placed successfully. Order ticket:")

def buyStop():
    
    print("buy Stop order placed successfully. Order ticket:")

def sellLimit():
    
    print("SellLimit order placed successfully. Order ticket:")

def blackSellLimit():

    print("Black SellLimit order placed successfully. Order ticket:")
     
def blackbuyLimit():
    print("Black buyLimit order placed successfully. Order ticket:")

def blackbuyStop():
    print("Black buyStop order placed successfully. Order ticket:")

def blackSellStop():
    print("Black SellStop order placed successfully. Order ticket:")

first_active = True
second_active = False
third_active = False
fourd_active = False
fifth_active = False
sixth_active = False
seventh_active = False

third = False
fourd = False
fifth = False
sixth = False
seven = False

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

#sellStop()
#sellStop()
buyLimit()
#buyStop()
#sellLimit()
last_price = startPrice

once_first = False
once_second = False
once_third = False 
once_fourd = False
once_fifth = False
once_sixth = False

#combination 2
'''sellStop(0, volume_2, 2)

#combination 3
sellStop(0, volume_3, 3)

#combination 4
sellStop(0, volume_4, 4)

#combination 5
sellStop(0, volume_5, 5)

#combination 6
sellStop(0, volume_6, 6)

#combination 7
sellStop(0, volume_7, 7)'''
fail = 0
failed_1 = False
failed_2 = False
failed_3 = False
failed_4 = False
failed_5 = False
failed_6 = False
failed_7 = False
once = False

x = 0
while fail != 1 and succes == False:

    
    if(x == 1):
        last_price += points
        last_price = round(last_price, 5)
        
    if(x == 2):
        last_price += points
        last_price = round(last_price, 5)
        
    if(x == 3):
        last_price += points
        last_price = round(last_price, 5)
       
    if(x == 4):
        last_price += points
        last_price = round(last_price, 5)
     
    if(x == 5):
        last_price += points
        last_price = round(last_price, 5)
    if(x == 6):
        last_price += points
        last_price = round(last_price, 5) 
       
    if(x == 7):
        last_price += points
        last_price = round(last_price, 5)

    if(x == 8):
        last_price += points
        last_price = round(last_price, 5)
    
    if(x == 9):
        last_price -= points*8
        last_price = round(last_price, 5)

    x += 1

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
        buyStop()
    
        once = True

    if(failed_7 == False):

        if(first_active_7 and last_price <= round(startPrice - points,5)):
            failed_7 = True
            first_active_7 = False
            cancel_SellStop_order(7,1)

        if(first_active_7 and last_price >= round(startPrice + points,5)):
            first_active_7 = False
            second_active_7 = True

        if(second_active_7 and last_price <= round(startPrice,5)):
            failed_7 = True
            second_active_7 = False
            cancel_SellStop_order(7,2)

        if(second_active_7 and last_price >= round(startPrice + points*2,5)):
            second_active_7 = False
            third_active_7 = True

        if(third_active_7 and last_price <= round(startPrice + points,5)):
            failed_7 = True
            third_active_7 = False
            cancel_SellStop_order(7,3)
        
        if(third_active_7 and last_price >= round(startPrice + points*3,5)):
            third_active_7 = False
            fourd_active_7 = True
        
        if(fourd_active_7 and last_price <= round(startPrice + points*2,5)):
            failed_7 = True
            fourd_active_7 = False
            cancel_SellStop_order(7,4)

        if(fourd_active_7 and last_price >= round(startPrice + points*4,5)):
            fourd_active_7 = False
            fifth_active_7 = True

        if(fifth_active_7 and last_price <= round(startPrice + points * 3,5)):
            failed_7 = True
            fifth_active_7 = False
            cancel_SellStop_order(7,5)

        if(fifth_active_7 and last_price >= round(startPrice + points*5,5)):
            fifth_active_7 = False
            sixth_active_7 = True
        
        if(sixth_active_7 and last_price <= round(startPrice + points*4,5)):
            failed_7 = True
            sixth_active_7 = False
            cancel_SellStop_order(7,6)
        
        if(sixth_active_7 and last_price >= round(startPrice + points*6,5)):
            sixth_active_7 = False
            seventh_active_7 = True
        
        if(seventh_active_7 and last_price <= round(startPrice + points*5,5)):
            seventh_active_7 = False
            failed_7 = True
            cancel_SellLimit_order(7,7)

        if(seventh_active_7 and last_price >= round(startPrice + points*7,5)):
            seventh_active_7 = False
            eight_active_7 = True

        if(eight_active_7 and last_price >= round(startPrice + points*8,5)):
            failed_7 = True
            eight_active = False
            cancel_buyLimit_order(7,8)

        if(eight_active_7 and last_price <= round(startPrice + points*6,5)):
           eight_active_7 = False
           nine_active_7 = True

        if(nine_active_7 and last_price <= round(startPrice - points,5)):
            nine_active_7 = False
            failed_7 = True

        if(nine_active_7 and last_price >= round(startPrice + points*8,5)):
            nine_active_7 = False
            print("Sell combination 7 finished")
            succes= True
    
        if(failed_7 == False):

            if(last_price >= round(startPrice + points,5) and third_7 == False and second_active_7):    
                buyStop()
                third_7 = True

            if(last_price >= round(startPrice + points*2,5) and fourd_7 == False and third_active_7):
                buyStop()
                fourd_7 = True

            if(last_price >= round(startPrice + points*3,5) and fifth_7 == False and fourd_active_7):
                buyStop()
                fifth_7 = True

            if(last_price >= round(startPrice + points*4,5) and sixth_7 == False and fifth_active_7):
                buyStop()
                sixth_7 = True

            if(last_price >= round(startPrice + points*5,5) and seventh_7 == False and sixth_active_7):
                buyStop()
                seventh_7 = True

            if(last_price >= round(startPrice + points*6,5) and eight_7 == False and seventh_active_7):
                sellLimit()
                eight_7 = True
            
            if(last_price <= round(startPrice + points*7,5) and nine_7 == False and eight_active_7):
                blackbuyLimit()
                nine_7 = True
        else :
            print("Sell Combination 7 failed")
            fail += 1