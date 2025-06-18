#shop program
#the shop of Mr Sakamoto
#the program will have two mode 1. Business , 2. Customer
item={"banana":{"price":24,"quantity":40}
      }
profit=0
def business_mode():
    global profit,item
    def add_item():

        while True:
            try:
                ask1=int(input("how many items you wanna add? "))
                break
            except ValueError:
                print("please type a valid entry")
        added=0
        while added<ask1:
            name=input("The name of the item you want to add :").lower()
            while True:
                try:
                    price=int(input("enter the price of your item :"))
                    qty=int(input(f"how many {name} :"))
                    break
                except ValueError:
                    print("enter a valid entry.")
            print(f"Successfully added")
            item[name]={"price":price,"quantity":qty}
            added+=1
    def view_items():
        print("......................................")
        print("------ Shop Inventory ------")
        for name, data in item.items():
            print(f"{name.capitalize()} Price :{data['price']} || Quantity :{data['quantity']}")
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
    global item,profit
    my_cash=500
    def view_items():
        print("......................................")
        print("------ Shop Inventory ------")
        for name, data in item.items():
            print(f"{name.capitalize()} Price :{data['price']} || Quantity :{data['quantity']}")
        print("......................................")
    def buying():
        global profit
        nonlocal my_cash
        cart={}
        while True:
            if len(item)==0:
                print("sorry we are out of items")
                break
            ask1=input("enter the name of your item// if finished shoppinng right 'nothing','exit' :").lower()
            if ask1=="nothing" or ask1=="exit":
                break
            if ask1 in item:
                ite=item[ask1]
                if ite['quantity']==0:
                    print("Out of stock")
                    continue
                while True:
                    try:
                        qty=int(input(f"how many {ask1.capitalize()}'s :"))
                        break
                    except ValueError:
                        print("enter something eligable")
                if qty>ite["quantity"]:
                    print(f"we dont have that many {ask1.capitalize()}")
                    continue
                total_price=ite["price"]*qty
                if my_cash<total_price:
                    print("poor bring more money")
                    continue
                my_cash-=total_price
                ite["quantity"]-=qty
                profit+=total_price 
                print(f"You purchased {ask1.capitalize()}s which was {total_price} BDT")
                print(f"now you got only {my_cash} BDT")
                    
                if ite["quantity"]==0:
                    del item[ask1]
            else:
                print("not found")
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
    if ask1 == "sakamoto" or ask1 == "mr sakamoto":
        business_mode()
    elif ask1=="customer":
        customer()
    elif ask1=="exit":
        print("Use us again. Bye bye")
        break
    else:
        print("incorrect!")
