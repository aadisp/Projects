MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources["money"]=0
def displayResource():
    print(f"\nWater: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}\n\n")

def checkResources():
    for item in MENU[order]["ingredients"]:
        if resources[item]<MENU[order]["ingredients"][item]:
            print(f"Not enough {item}")
            return "stop"
    return "proceed"

def checkPrice():
    print(f"\nThe {order} is going to cost you ${MENU[order]["cost"]}")
    print("Insert your coins:")
    quarters=int(input("Quarters: "))*0.25
    dimes=int(input("Dimes: "))*0.1
    nickels=int(input("Nickels: "))*0.05
    pennies=int(input("Pennies: "))*0.01
    total=quarters+dimes+nickels+pennies
    if total<MENU[order]["cost"]:
        print(f"You are short by {MENU[order]["cost"]-total}")
        return "stop"
    elif MENU[order]["cost"]<total:
        print(f"Here's your change: {round((total-MENU[order]["cost"]),2)}")
        revenue=round((total-MENU[order]["cost"]),2)
        resources["money"]=revenue
        return "proceed"
    else:
        revenue = total
        resources["money"] = revenue
        return "proceed"

def resourceDeplete():
    for item in MENU[order]["ingredients"]:
        if resources[item]-MENU[order]["ingredients"][item]>=0:
            resources[item] -= MENU[order]["ingredients"][item]
        else:
            resources[item]=0


machine='on'
while machine!='off':
    orderNumber=input("""What would you like to have?
    Espresso [1]
    Latte [2]
    Cappuccino[3]
  """)
    order=''
    if orderNumber=="1":
        order="espresso"
    elif orderNumber=="2":
        order="latte"
    elif orderNumber=="3":
        order="cappuccino"
    elif orderNumber=="REPORT":
        displayResource()
    elif orderNumber=="off":
        print("\nTurning off")
        machine=orderNumber
        print("\nThank you")

    if order!='':
        permission=checkResources()
        if permission=="proceed":
            permission=checkPrice()
            if permission == "proceed":
                resourceDeplete()
                print(f"\nEnjoy your {order}!")
                print("\n"*2)
