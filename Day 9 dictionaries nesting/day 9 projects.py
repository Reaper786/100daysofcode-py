# from Logo import logo
#
# bidding = {}
#
# while True:
#     from os import name, system
#
#
#
#
#     def add_new_bidder(name, amount):
#
#         bidder_name = name
#         bidder_amount = int(amount)
#         bidding[bidder_name] = bidder_amount
#
#     print(logo)
#
#
#     bidder_name = input("Please enter your name?\n".lower())
#     bidder_amount = int(input("please enter the amount? R "))
#
#     add_new_bidder(name=bidder_name, amount=bidder_amount)
#
#     additional = input("Is there another bidder? y or n?\n".lower())
#
#     winning_bidder = {}
#
#     if additional == "y" or additional == "yes":
#         print('\n' * 80)  # prints 80 line breaks
#         continue
#     else:
#
#         print(bidding)

######################################################################################

from Logo import logo

print(logo)

print("Welcome to secret Auction")

bids = {}
bidding_finish = False


def find_highest_bidder(bidding_record):
    #bidding_record = {"angela": 123, "james": 321}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of R {highest_bid}")

while not bidding_finish:
    name = input("What is your name? ")
    price = int(input("What is your bid? R "))
    bids[name] = price

    should_continue = input("Are there any other bidders? type 'yes' or 'no'.".lower())
    if should_continue == "no":
        bidding_finish = True
        find_highest_bidder(bidding_record=bids)
    elif should_continue == "yes":
        clear()






