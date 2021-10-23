# # Day 5 - 1 - exercise - average height
#
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# # 🚨 Don't change the code above 👆
#
#
# #Write your code below this row 👇
#
# total_height = 0
# for height in student_heights:
#   total_height = total_height + height
#
# students_amount = 0
# for students in student_heights:
#   students_amount += 1
#
# average = round(total_height/students_amount)
# print(f"Average Height: {average}")

#######################################################################################

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
#
# print(f" The highest score in class is: {highest_score}")

#######################################################################################

# # Day 5 -3 adding evens
#
# total = 0
#
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)
#
# ## what the lecturer did
#
# total = 0
#
# for number in range(2, 101, 2):
#         total += number
# print(total)

#######################################################################################

# Day 5 -4 fuzz
#
# for number in range (1,101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("fizzbuzz")
#   elif number % 3 == 0:
#     print("fizz")
#   elif number % 5 == 0:
#     print("buzz")
#   else:
#     print(number)

#######################################################################################

