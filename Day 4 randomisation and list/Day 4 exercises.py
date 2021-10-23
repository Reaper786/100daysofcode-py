# Day 4 -1 heads or tails

# import random
#
# random_integer = random.randint(0, 1)
#
# if random_integer == 1:
#     print("it's Heads")
# else:
#     print("it's Tails")

#######################################################################

# # Day 4 -2 - banker roulette
#
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇

# first attempt
# import random
# #
# # banker = random.choice(names)
# #
# # print(f"The Banker today will be {banker}")
#
# # second attempt
#
# amount_names = len(names)
#
# banker = random.randint(0, (amount_names - 1))
#
# banker_name = names[banker]
#
# print(f"Your banker will be {banker_name}")

#######################################################################

# # Day 4 -3 treasure map
#
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
#
# position_1 = int(position[0]) - 1
# position_2 = int(position[1]) - 1
#
# map[position_1][position_2] = " X "
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
#######################################################################

