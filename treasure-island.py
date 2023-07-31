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

response = input("You are at a crossroad. Where do you want to go? 'left' or 'right'?\n")

if response.upper() == "LEFT":
  response1 = input("You have come to a riverbank.You can either swim across or wait for a boat. What do you want to do? 'swim' or 'wait'?\n")
  
  if response1.upper() == "WAIT":
    response2 = input("Patience has brought you this far. There are three doors here. Which door do you want to enter? 'red' or 'blue' or 'yellow'?\n")
    
    if response2.upper() == "RED":
      print("You have been burned by fire. Game Over!")
    elif response2.upper() == "BLUE":
      print("You have been eaten by Beasts. Game Over!")
    elif response2.upper() == "YELLOW":
      print("You found the treasure. You Win!")
    else:
      print("Game Over!")
      
  else:
    print("Your impatience didn't pay off. You have been attacked by trout! Game Over.")
    
else:
  print("You made the wrong turn. You have fallen into a hole! Game Over.")