from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True
Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
while machine_on:
    choice = input(f"What would you like? ({Menu.get_items()}): ")

    if choice == "off":
        machine_on = False
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(drink):
            if MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)




