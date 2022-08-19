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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

choice_one = input(
    "You come across a fork, which direction do you choose? left or right? ").lower()
if(choice_one == "left"):
    choice_two = input(
        "You come across a pond, do you wait, or swim across? ").lower()
    if(choice_two == "wait"):
        print("The water rapidly dries up revealing three doors!")
        choice_three = input("Pick a door: Red, Blue, Yellow ").lower()
        if(choice_three == "yellow"):
            print("You found the treasure! YOU HAVE FOUND ONE PIECE.")
        elif (choice_three == "red"):
            print("You are transported to a room filled with fire and meteors!\n Looking behind you, the door has disappeared! \n Suddenly a meteor has fallen from the sky and hits you! You have died!")
        elif (choice_three == "blue"):
            print("The blue door disappears and you are instantly transported into a dark room. \n The room rapidly fills up with water and you drown! Game Over!")
        else: 
          print("Your indecision has cost you your life! Game over!")   
    else:
        print("Piranhas leap out of the water and eat you up! Game Over!")
else:
    print("You fell into an endless pit. Game over. Restart the game.")
