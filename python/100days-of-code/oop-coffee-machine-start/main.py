from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


isRunning = True

while isRunning:
    options = menu.get_items()
    select = input(f"What would you like? ({options}): ")
    select = select.title()
    if select == "Off":
        isRunning = False
    elif select == "Report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(select.lower())
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

