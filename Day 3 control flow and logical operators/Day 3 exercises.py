# # day 3 - 1 - Odd or even
#
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# first_input = int(number % 2)
#
# if first_input == 1:
#     print("This number is Odd!")
# else:
#     print("This number is Even!")

#################################################################################################

# day 3 - 2 - BMI 2.0

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# floated_result = (float(weight) / (float(height) ** 2))
# BMI = round(floated_result, 1)
#
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, You are underweight, please eat more!")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, You are in the normal weight range")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, You are slightly overweight, try to reduce the food intake!")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, You are Obese, please reduce food intake and go gym!")
# else:
#     print(f"Your BMI is {BMI}, You are clinical Obese, please consult your doctor or Dietitian!!!")

#################################################################################################
# # day 3 - 3 - leap year
#
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

#################################################################################################

# Day 3 control flow and logical operators -4 - Pizza order

# print("Good day, Welcome to H3 Pizzaria")
# print("The Menu")
#
# print("Small Pizza (S): R 20")
# print("Medium Pizza (M): R 60")
# print("Large Pizza (L): R 100 ")
#
# bill = 0
#
# pizza = input("Please select the size of your pizza: (S, M or L)\n")
#
# if pizza == "S" or "s":
#     bill = 20
#     pep = input("Would you like to add Pepperoni to your pizza? (Y/N)\n")
#     if pep == "Y" or "y":
#         bill += 2
#         cheese = input("Would you like to add Cheese to your pizza? (Y/N)\n")
#         if cheese == "Y" or "y":
#             bill += 1
#
# elif pizza == "M" or "m":
#     bill = 60
#     pep = input("Would you like to add Pepperoni to your pizza?\n")
#     if pep == "Y" or "y":
#         bill += 3
#         cheese = input("Would you like to add Cheese to your pizza? (Y/N)\n")
#         if cheese == "Y" or "y":
#             bill += 1
#
# elif pizza == "L" or "l":
#     bill = 100
#     pep = input("Would you like to add Pepperoni to your pizza?\n")
#     if pep == "Y" or "y":
#         bill += 3
#         cheese = input("Would you like to add Cheese to your pizza? (Y/N)\n")
#         if cheese == "Y" or "y":
#             bill += 1
# else:
#     print("invalid option: Error code 69")
#
# if bill > 0:
#     if input(f"Your total is {bill}, Would you like to complete the order? Y/N\n") == "Y" or "y":
#         print("Your order is being prepared! we will call your number as soon as it is done :) enjoy")
# else:
#     print("Please restart the application as an error was identified!")

#################################################################################################

# # Day 3 control flow and logical operators- 5 - Love Calculator
#
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# lower_n1 = name1.lower()
# lower_n2 = name2.lower()
#
# T1 = lower_n1.count("t")
# R1 = lower_n1.count("r")
# U1 = lower_n1.count("u")
# E1 = lower_n1.count("e")
#
# L1 = lower_n1.count("l")
# O1 = lower_n1.count("o")
# V1 = lower_n1.count("v")
# E1_1 = lower_n1.count("e")
#
# T2 = lower_n2.count("t")
# R2 = lower_n2.count("r")
# U2 = lower_n2.count("u")
# E2 = lower_n2.count("e")
#
# L2 = lower_n2.count("l")
# O2 = lower_n2.count("o")
# V2 = lower_n2.count("v")
# E2_1 = lower_n2.count("e")
#
# TT = int(T1) + int(T2)
# print(f"The letter T appeared: {TT} times.")
# RR = int(R1) + int(R2)
# print(f"The letter R appeared: {RR} times.")
# UU = int(U1) + int(U2)
# print(f"The letter U appeared: {UU} times.")
# EE = int(E1) + int(E2)
# print(f"The letter E appeared: {EE} times.")
#
# Total_true = TT + RR + UU + EE
#
# print(f"The total for True: {Total_true}")
#
# LL = int(L1) + int(L2)
# print(f"The letter L appeared: {LL} times.")
# OO = int(O1) + int(O2)
# print(f"The letter O appeared: {OO} times.")
# VV = int(V1) + int(V2)
# print(f"The letter V appeared: {VV} times.")
# EE1 = int(E1_1) + int(E2_1)
# print(f"The letter E appeared: {EE1} times.")
#
# Total_love = LL + OO + VV + EE1
#
# print(f"The total for True: {Total_love}")
#
# Love_amount = Total_love + Total_true
#
# if Love_amount < 10 or Love_amount > 90:
#     print(f"Your love score is {Love_amount}, you go together like coke and mentos")
# elif Love_amount >= 40 and Love_amount <=50:
#     print(f"Your Love score is {Love_amount}, You guys go together!!!")
# else:
#     print(f"Your love score is {Love_amount}.")