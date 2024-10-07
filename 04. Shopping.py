def database():
    global cartz
    global lower
    global tshirt
    global shirt
    lower = tshirt = shirt = 0
    cartz = {
        "lower": 0,
        "shirt": 0,
        "tshirt": 0 
    }

def main():
    who = input("Press c If you are customer , press P if you are a producer and e to exit : ")
    if who == "c":
        customer()
    elif who == "p":
        producer()
    elif who == "e":
        print("Thank You For Choosing Us")
    else:
        print("Wrong Input")
        main()

def producer():
    global lower
    global tshirt
    global  shirt
    product = input(" Press l if you want to produce lower\n Press t if you want to produce tshirt\n Press s if you want to produce shirt\n ")
    

    
    if product == "l":
        num = int(input("Enter the no of Lower you want to produce: "))
        lower += num
        print(f"Available lowers are {lower}, shirts are {shirt} and tshirt are {tshirt}")
        again = (input("Press 1 if you want to produce again : "))
        if again == '1' :
            producer()
        else:
            main()
    elif product == "t":
        num = int(input("Enter the no of tshirt you want to produce : "))
        tshirt += num
        print(f"Available lowers are {lower}, shirts are {shirt} and tshirt are {tshirt}")
        again = int(input("Press 1 if you want to produce again : "))
        if again == 1 :
            producer()
        else:
            main()
    elif product == "s":
        num = int(input("Enter the no of shirt you want to produce : "))
        shirt += num
        print(f"Available lowers are {lower}, shirts are {shirt} and tshirt are {tshirt}")
        again = int(input("Press 1 if you want to produce again : "))
        if again == 1 :
            producer()
        else:
            main()
    else:
        print("Wrong Input")
        producer()


    

def customer():
    choice = input("Press buy  a to add to cart or t to track your or b to buy and e to exit  : ")
    if choice == "a":
        prod = input(" Press l for Lower \n Press t for tshirt \n Press s for shirt\n  : ")

        if prod == "l":
            num = int(input("How many lower you want : "))
            if num > lower:
                print("These no of lowers are not available")
            else:
                cart(prod , num)    
        elif prod == "t":
            num = int(input("How many tshirt you want : "))
            customer()
            if num > tshirt:
                print("These no of tshirts are not available")
            else:
                cart(prod , num)
        elif prod == "s":
            if num > shirt:
                print("These no of shirts are not available")
            else:
                cart(prod , num)
        else:
            print("Wrong Input")
    elif choice == "t":
        track()
    elif choice == "b":
        Buy()
    elif choice == "e":
        print("Thank You For Choosing Us")
    else:
        print("Wrong Input")
        customer()
        

def cart(P,N):
    global cartz
    if P == "l":
        cartz["lower"] = N
        main()
    elif P == "t":
        cartz["tshirt"] = N
        main()
    elif P == "s":
        cartz["shirt"] = N
        main()

def Buy():
    global cartz
    global lower
    global shirt
    global tshirt

    if cartz["lower"] == 0 and cartz["shirt"] == 0 and cartz["tshirt"] == 0:
        print("Enter something to cart before buying ")
    else:
        lower -= cartz["lower"]
        shirt -= cartz["shirt"]
        tshirt -= cartz["tshirt"]
        print("Thanks For Shopping Whith Us")
        cartz["lower"] == 0 and cartz["shirt"] == 0 and cartz["tshirt"] == 0


def track():
    print(f"lower: {cartz['lower']}, tshirts: {cartz['tshirt']}, shirts :{cartz['shirt']}")


database()
main()

