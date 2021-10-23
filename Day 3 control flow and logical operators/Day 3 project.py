print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# NPC corner
NPCMJ = "Mercenary jake"

print(f"{NPCMJ}: Good Morning young dungeon crawler,")
print(f"{NPCMJ}: What is your name young one?")

# player name
name = input("Please provide a name? ")

print(f"{NPCMJ}: Hi, {name}, I am Mercenary Jake, ")
print(f"{NPCMJ}: let's head on out!")

d1 = input("Would you like to exit north gate (1) or south gate (2)")

if d1 == "1":
    print("You end up at a crossroad, on the sign it shows:")
    print("please input your choice? (1, 2)")

    d2 = input("left forest? and right lake?")

    if d2 == "2":
        print("you end up at then lake's boat dock, ")
        print("would you like to wait for a boat or swim")

        d3 = input("Swim or wait? (1, 2) ")

        if d3 == "2":
            print("A boat arrived and you jump on it")
            print("You have arrived at the island in the middle of the lake safely, ")
            print("you see a sign advising to select 1 of the 3 cave entrances")

            d4 = input("Select left, middle or right: (1,2 or3)  ")

            if d4 == "1":
                print("You walk into the cave, you see a warm glow as you walking deeper")
                print("as you reach the light, a brightness from the light dissipates")
                print("what you see amazes you, you look around seeing")

                dest = input("enter you fantasy?")

                print(f"{dest} everywhere, your eyes tear and a big smile on your face as you find your dream")

            elif d4 == "2":
                print("A surprise ambush by thieves as you walk into their den")
                print("you get robbed and killed")

            else:
                print("you get killed by a dragon which was sleeping in the cave!")

        else:
            print("you attempted to swim, but the lake demon killed you.")

    else:
        print("as your walking into the forest you hear growling, ")
        print("as you turn around, you see sharp teeth above your head as a wolf pounced")
        print("you have died!")

else:
    print("as you walking down the south path, a mysterious fog surrounds you")
    print("you continue to walk, however you have a strange feeling you getting watches")

    d5 = input("continue or turn back? (1, 2) ")

    if d5 == "2":
        print("as you turn around, you see a shadow running towards you and start feeling cold")
        print("you look down and see a blade in your chest")

    else:
        print("as you continue, the shadows multiply")
        print("you hear a giggling right behind you")
        print("as you turn around, your eyes face upwards")
        print("you see your body headless, as your eyes close")
        print("you see blood drenched sword and shadow figure with a smile")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
