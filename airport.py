#packaging bag to airport management to secururity check to plane to destiny
#it is game with obsticle 
import random
import time
def backpack():
    rank=["1st","2nd","3rd","4th","5th"]
    print("You have a few items here. For your journey you can pick 4 item from any of these")
    print("Items to pick from : ",", ".join(mixed_item))
    i=0
    while i<4:
        choosing_item=input(f"enter the {rank[i]} item :")
        if choosing_item not in mixed_item:
            print("no!")
        else:
            user_item.append(choosing_item)
            i+=1
    print("backpack done!")
    print("you choose :",", ".join(user_item))
    
    return True
def ticket_cutting():
    global name,title
    seat_num=["14B","15C","18D","20A","10B"]
    seat_num=random.choice(seat_num)
    while True:
        try:
            name=input("what is your name :")
            age=int(input("enter your age :"))
            gender=input("male or female :").lower()
            break
        except ValueError:
            print("Enter a Valid input!")
    
    if gender not in ["male","female"]:
        print(f"Mf bitch we dont allow {gender} in our airlines")
        return False
    
    if gender=="male":
        title="Mr."
    else:
        title="Ms."

    if age<18:
        print("where is your mom? You cannot travel in this age idiot go watch hentai")
        return False
    else:
        print(f"{title} {name.capitalize()}, welcome!")
    
    
    countries=["dubai","paris","new york","delhi","istanbul"]
    print("Now that you finished packing bag. Now choose where you want to go to")
    print("Dubai")
    print("New York")
    print("Delhi")
    print("Paris")
    print("Istanbul")
    while True:
        ask1=input("which country :")
        if ask1 not in countries:
            print(f"we dont go to {ask1} country")
        elif ask1 in countries:
            print(f"Heading to {ask1.capitalize()}")
            print("You will be using US Bangla airlines")
            print("")
            print("-----Boarding Pass-----")
            print(" US Bangla Air lines ")
            print(f"     Name :{name.capitalize()}")
            print(f"     Age :{age}")
            print(f"     Gender: {gender.capitalize()}")
            print(f"Destination :{ask1.capitalize()}")
            print("     number of seats: 01")
            print(f"     Seat number: {seat_num}")
            break
        else:
            print("bozzo wrong")

    return True

def security_entering():
    global user_item,not_allowed_items,name,title
    print("........................................")
    print(f"{title} {name.capitalize()}, Welcome to security check")
    print("you can either type show or no")
    ask1=input("Cops:  Show your bag or not :")
    while True:
        if ask1=="show":
            break
        elif ask1=="no":
            print("You joking? Leave airport now!")
            return False
        else:
            print("enter a correct value")
    print("Checking your items in 3 seconds")
    for i in range(3,0,-1):
        time.sleep(1)
    common_item=set(user_item)&set(not_allowed_items)
    if common_item:
        print("!!!!!!!!!!!!!!")
        print("WARNING")
        print(f"How dare you bring ",",".join(common_item))
        print("You are arrested and not alllowed to go any further")
        return False
    else:
        print("You are free to go.")
        print("Game done")
        return True
    
name=""
title=""
user_item=[]
allowed_items=["laptop","shirt","pajamas","underwear","books","playstation","beer"]
not_allowed_items=["iron","drone","gun","wine","shampoo"]
mixed_item=allowed_items+not_allowed_items
random.shuffle(mixed_item)
if backpack():
    if ticket_cutting():
        if security_entering():
            print("all done")