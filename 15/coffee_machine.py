from coffee_data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coin_value = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

# Print Report: shows resources remaining
# Check resources are sufficient when making a drink
# Process Coins - Refund money if not enough
# Calculate the amount of coins + change when putting in the correct amount of coins
# Update the resources when making coffee


def subtract_money(money, cost):
    return money - cost


def print_report():
    print(f"Resources remaining:")
    for key in resources:
        if key == 'coffee':
            print(f"{key.capitalize()}: {resources[key]}g")
        elif key == 'water' or key == 'milk':
            print(f"{key.capitalize()}: {resources[key]}ml")
        elif key == "money":
            print(f"Money: ${resources[key]}")


def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(
                "Sorry, this machine doesn't have enough ingredients to make your coffee.")
            return False
    return True


def make_coffee(coffee_type: str, quarters: int = 0, dimes: int = 0, nickles: int = 0, pennies: int = 0):
    """coffee_type takes in the following values: 'espresso/latte/cappuccino'\n
       Quarters, Dimes, Nickles and Pennies take in an integer value. 
    """
    drink = MENU[coffee_type]
    coffee_price = drink["cost"]
    total_money_entered = (coin_value["quarter"] * quarters) + (coin_value["dime"] * dimes) + (
        coin_value["nickle"] * nickles) + (coin_value["penny"] * pennies)
    change = total_money_entered % coffee_price
    if coffee_type in MENU:
        if total_money_entered < coffee_price:
            print("Insufficient funds!")
            return False
        elif total_money_entered >= coffee_price:
            if not check_resources(drink["ingredients"]):
                return
            else:
                resources["money"] += coffee_price
                resources["water"] -= drink["ingredients"]["water"]
                resources["coffee"] -= drink["ingredients"]["coffee"]
                change = round((total_money_entered - coffee_price), 2)
                print(resources)
                if change:
                    print(f"Here's your change: ${'{:.2f}'.format(change)}.")
    else:
        print("Please choose a valid coffee type!")
        coffee_choice = input("What flavor would you like? 'espresso/")
        quarters = int(input("How many quarters do you want to use?\n"))
        dimes = int(input("How many dimes do you want to use?\n"))
        nickles = int(input("How many nickles do you want to use?\n"))
        pennies = int(input("How many pennies do you want to use?\n"))
        make_coffee(coffee_choice, quarters, dimes, nickles, pennies)


def start_machine():
    using_machine = True
    while using_machine:
        user_choice = input(
            "Do you want to use the coffee machine? Type: 'y' or 'n'\n").lower()
        if user_choice == 'y':
            print("Then we shall keep making coffee!!!!")
        elif user_choice == 'report':
            print_report()
            start_machine()
        else:
            using_machine = False
            print("Have a good day!")
            break
        coffee_choice = input(
            "What flavor would you like? 'espresso/latte/cappuccino\n").lower()
        if coffee_choice == 'report':
            start_machine()
            resources["water"] -= 25
        quarters = int(input("How many quarters do you want to use?\n"))
        dimes = int(input("How many dimes do you want to use?\n"))
        nickles = int(input("How many nickles do you want to use?\n"))
        pennies = int(input("How many pennies do you want to use?\n"))
        make_coffee(coffee_choice, quarters, dimes, nickles, pennies)


start_machine()
