from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report
# check resources are sufficient
# process coins
# check transaction successful?
# make Coffee
coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def start_machine():
    using_machine = True
    while using_machine:
        answer = input("Would you like some coffee? Press 'y' or 'n'\n")
        if answer == 'y':
            choice = input(
                f"What would you like to have? {coffee_menu.get_items()}\n")
            drink = coffee_menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        elif answer == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            print("Goodbye!")
            using_machine = False


start_machine()
