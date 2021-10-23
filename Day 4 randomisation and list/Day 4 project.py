import random

print("Welcome to my little game of rock paper scissors :)")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_choice = [rock, paper, scissors]
player_input = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors \n")
if player_input >= 3 or player_input < 0:
    print("invalid input: 69")
    player_choice = list_choice[int(player_input)]
    print(player_choice)

    print("I will now select :)")

    computer_turn = len(list_choice)
    random_choice = random.randint(0, (int(computer_turn)) - 1)
    computer_choice = list_choice[random_choice]
    print(computer_choice)

    # if player_choice == computer_choice:
    #     print("This is a draw!!!")
    # else:
    #     if player_choice == 0 and computer_choice == 2:
    #         print("Player wins!!!")
    #     else:
    #         if player_choice == 1 and computer_choice == 0:
    #             print("Player wins!!!")
    #         else:
    #             if player_choice == 2 and computer_choice == 1:
    #                 print("Player wins!!!")
    #             else:
    #                 print("Computer Wins!!!")

    if player_choice == 0 and computer_choice == 2:
        print("Player wins!!!")
    elif computer_choice == 0 and player_choice == 2:
        print("computer wins!!")
    elif computer_choice > player_choice:
        print("computer wins!!")
    elif player_choice > computer_choice:
        print("Player wins!!!")
    elif player_choice == computer_choice:
        print("Its a draw")

