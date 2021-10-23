from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    client_choice = input(f"Please select from the list of available drinks? ({options})")
    if client_choice == "off":
        is_on = False
    elif client_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(client_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


