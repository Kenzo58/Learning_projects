#shop program
#the shop of Mr Sakamoto
#the program will have two mode 1. Business , 2. Customer
item={"banana":24}
def business_mode():

    def add_item():
        while True:
            try:
                ask1=int(input("how many items you wanna add? "))
                break
            except ValueError:
                print("please type a valid entry")

        while True:
            if len(item)==ask1:
                print(f"Your {ask1} items added to shop!")
                break
            ask2=input("The name of the item you want to add :").lower()
            ask3=int(input("enter the price of your item :"))
            item[ask2]=ask3
    def view_items():
        print("......................................")
        for x,y in item.items():
            print(f"{x} - {y}")
        print("......................................")
    while True:
        try:
            print("......................................")
            print("Welcome Mr Sakamoto")
            print("For adding item type 1")
            print("For viewing item type 2")
            print("type 3 for going back to menu")
            print("......................................")
            choice=int(input("which :"))
        except ValueError:
            print("please type a valid entry")
        if choice==1:
            add_item()
        elif choice==2:
            view_items()
        elif choice==3:
            break
        else:
            print("incorrect!")
def customer():
    def view_items():
        print("......................................")
        for x,y in item.items():
            print(f"Name :{x} - Price :{y}")
        print("......................................")
    def buying():
        while True:
            if len(item)==0:
                print("sorry we are out of items")
                break
            ask1=input("enter the name of your item/if finished shoppinng right 'nothing','exit' :").lower()
            if ask1 in item:
                del item[ask1]
                print(f"purchased {ask1.capitalize()}")
                continue
            elif ask1=="nothing" or ask1=="exit":
                print("Thanks for coming to Sakamoto shop!")
                break
            else:
                print("Item unavailable!")
                print("check our items again :")
                for x,y in item.items():
                    print(f"Name :{x} - Price: {y}")
    while True:
        try:
            print("......................................")
            print("For viewing item type 1")
            print("For buying item type 2")
            print("type 3 for going back to menu")
            print("......................................")
            choice=int(input("which :"))
        except ValueError:
            print("please type a valid entry")
        if choice==1:
            view_items()
        elif choice==2:
            buying()
        elif choice==3:
            break
        else:
            print("incorrect!")

while True:
    print("......................................")
    print("Welcome to the shop of Mr Sakamoto!")
    print("if you want to exit then type 'exit' ")
    print("......................................")
    try:
        ask1=input("Are you Mr Sakamoto or a customer? :").lower()
    except ValueError:
        print("write a valid input")
    if ask1=="sakamoto" or ask1=="mr sakamoto":
        business_mode()
    elif ask1=="customer":
        customer()
    elif ask1=="exit":
        print("Use us again. Bye bye")
        break
    else:
        print("incorrect!")
