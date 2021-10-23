# day 8- 1 paint
#
# # Write your code below this line 👇
# import math
#
#
# def paint_calc(height, width, cover):
#     area = (height * width) / cover
#     rounded_cans = math.ceil(area)
#     print(f"You'll need {rounded_cans} cans of paint")
#
#
# print("Paint coverage test")
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

##############################################################################################################

# day 8 -2 prime checker

# Write your code below this line 👇

# my code:

# def prime_checker(number):
#     a = []
#     while number % 2 == 0:
#         a.append(2)
#         number /= 2
#     f = 3
#     while f * f <= number:
#         if number % f == 0:
#             a.append(f)
#             number /= f
#         else:
#             f += 2
#     if number != 1:
#         a.append(number)
#     if a[0] == number:
#         print("this is a prime number")
#     else:
#         print("this is not a prime number")

# lecturers code

def prime_checker(number):
    is_prime =  True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

##############################################################################################################
