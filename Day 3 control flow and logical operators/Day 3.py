# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("continue")
#
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("Welcome to the scariest ride you ever been on. Enjoy!!!")
    age = int(input("Please provide your age?\n"))
    if age < 12:
        bill = 50
        print("Child ticket = R 50")
    elif age < 18:
        bill = 100
        print("Youth ticket = R 100")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Midlife ticket = R 0")
    else:
        bill = 150
        print("Adult ticket = R 150")

    photo_with = input("Would you like a photo with your ticket? (Y or N)\n")
    if photo_with == "Y" or "y":
        bill += 3

    print(f"Your final bill is R {bill}")

else:
    print("Sorry, I'm afraid you unable to ride this rollercoaster. :( ")



