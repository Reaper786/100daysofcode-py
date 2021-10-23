##############################Coffee Machine####################################

from Art import logo
from menu import MENU

# Prompt user by asking “ What would you like? (espresso/latte/cappuccino):

print(logo)

coffee_mug = "☕"

# Turn off the Coffee Machine by entering “ off ” to the prompt.

power_up = True

water = 1000
milk = 500
coffee = 150
money = 0

while power_up:

    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    # Print report

    if user_choice == "report":
        print(f"""
            water   : {water}ml
            milk    : {milk}ml
            coffee  : {coffee}g
            Money   : R{money}
        """)

    if user_choice == "refill":
        if 0 < water < 50:
            water = 1000
        elif 0 < milk < 50:
            milk = 500
        elif 0 < coffee < 18:
            coffee = 150

    if user_choice == "off":
        power_up = False

    # Check resources sufficient and making

    if user_choice == "latte" or user_choice == "cappuccino" or user_choice == "espresso":
        recipe = MENU[user_choice]
        recipe_preing = recipe["ingredients"]
        recipe_milk = recipe_preing["milk"]
        recipe_water = recipe_preing["water"]
        recipe_coffee = recipe_preing["coffee"]
        print("Please insert coins")
        coin_check_quarters = int(input("How much quarters?\n"))
        coin_check_dimes = int(input("How much dimes?\n"))
        coin_check_nickles = int(input("How much nickles?\n"))
        coin_check_pennies = int(input("How much pennies?\n"))
        Total = float((coin_check_pennies * 0.25) + (coin_check_dimes * 0.10) + (coin_check_nickles * 0.05) + (
                coin_check_pennies * 0.01))
        Total_amount = round(Total, 2)
        if Total_amount >= recipe["cost"]:
            change = round(Total_amount - recipe["cost"], 2)
            print(f"Total inserted money: ${Total_amount}, your change will be ${change}")
            if recipe["cost"] > Total_amount:
                print(f"Sorry, but you gave to little money, refund {Total_amount}")
            elif recipe_milk > milk or recipe_coffee > coffee or recipe_water > water:
                print(
                    f"We apologize for the inconvenience, your money will be refunded, total ${Total_amount}, please "
                    f"refill")
            else:
                milk -= recipe_milk
                coffee -= recipe_coffee
                water -= recipe_water
                money += recipe["cost"]
                print(
                    f"Thank you for your purchase, please remove your {coffee_mug}{user_choice} and enjoy your day "
                    f"further")
                print(f"Please remember to take your change: ${change}")

###############################lecturer code######################################################
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
