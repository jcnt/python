import os
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

vault = 0

def check_resources(item):
    for key in resources: 
      if MENU[item]['ingredients'][key] >= resources[key]:
        print(f"There's not enough {key} in the machine")
        return("fail")
    return("OK")

def coins(item):
    money = int(input("\nHow many quarters? ")) * 0.25
    money += int(input("How many dimes? ")) * 0.10
    money += int(input("How many nickles? ")) * 0.05
    money += int(input("How many pennies? ")) * 0.01
    if MENU[item]['cost'] > money:
        return("fail")
    else:
        change = round(money - MENU[item]['cost'], 2)
        print(f"\n\nYour change is ${change}")
        return(change)

def mkcoffee(item):
    global vault
    for key in resources:
        resources[key] -= MENU[item]['ingredients'][key] 
    vault += MENU[item]['cost'] 
    print(f"\n\nHere's your {item.title()}, Enjoy!")
    
is_running = True

while is_running: 
    os.system('clear')
    usersel = input("\n\nESPRESSO MACHINE MENU\n\n\nWhat would you like? Espresso/Latte/Cappuccino ")
    
    if usersel.title() == "Espresso":
        item = usersel.lower()
        if check_resources(item) == "OK":
            change = coins(item)
            if change == "fail":
                print("That's not enough money, sorry")
            else:
                mkcoffee(item)
        time.sleep(3)

    elif usersel.title() == "Latte":
        item = usersel.lower()
        if check_resources(item) == "OK":
            change = coins(item)
            if change == "fail":
                print("That's not enough money, sorry")
            else:
                mkcoffee(item)
        time.sleep(3)
    
    elif usersel.title() == "Cappuccino":
        item = usersel.lower()
        if check_resources(item) == "OK":
            change = coins(item)
            if change == "fail":
                print("That's not enough money, sorry")
            else:
                mkcoffee(item)
        time.sleep(3)
        
    elif usersel == "off":
        is_running = False
    
    elif usersel == "report":
        print(f"\nWater: {resources['water']}ml\nMilk:  {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${vault}\n")
        time.sleep(3)
    
    else:
        print("Wrong selection.")
        time.sleep(3)
    
    
