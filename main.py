from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

status = "on"

while status != "off":
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ")
    if choice == "off":
        status = "off"
    elif choice == "report":
        coffeeMachine.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMachine.make_coffee(drink)                        