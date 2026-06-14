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

def displayResource():
    print(f"water: {resources["water"]}ml")
    print(f"milk: {resources["milk"]}ml")
    print(f"coffee: {resources["coffee"]}g")

def checkResources():
    for item in MENU["espresso"]["ingredients"]:
        if resources[item]>=MENU["espresso"]["ingredients"][item]:
            print(f"{item} Ok")
        else:
            print(f"{item} Not")
