print("Welcome to the bill calculator!!!")
print("We aim to make your life a little easier :)\n")

bill = input("Please enter your bill amount? R ")
tip = input("Please enter the amount you would like to add for a tip? eg 10, 12 or 15: ")
amount_of_people = input("Please enter the amount of people in your party? ")

tip_percent = int(tip) / 100
floated_tip = float(tip_percent)
total = float(bill) * float(1 + floated_tip)
rounded_total = round(total, 2)
divided_total = float(rounded_total) / int(amount_of_people)
# final_amount = round(divided_total, 2)
# instead of using round - use {:.2f} (above code use below)
final_amount = "{:.2f}".format(divided_total)

print(f"Each person should be paying total of: R {final_amount}")