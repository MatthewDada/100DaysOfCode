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

#Write your code below this line 👇
import random 


rock = 0
paper = 1
scissors = 2

print("Welcome to the Rock-Paper-Scissors game.")
choice = input("Enter 0 for rock, 1 for paper, or 2 for scissors\n")

computer_random_choice = random.randint(0,2)

if choice == "0":
  if computer_random_choice == 0:
    print("It is a tie! You both picked Rock.")
  elif computer_random_choice == 1:
    print("You lose! Computer's choice is Paper.")
  else:
    print("You win! Computer's choice is Scissors.")

elif choice == "1":
  if computer_random_choice == 0:
    print("You win! Computer's choice is Rock.")
  elif computer_random_choice == 1:
    print("It is a tie! You both picked Paper.")
  else: 
    print("You lose! Computer's choice is Scissors.") 

elif choice == "2":
  if computer_random_choice == 0:
    print("You lose! Computer's choice is Rock.") 
  elif computer_random_choice == 1:
    print("You win! Computer's choice is Paper.")
  else:
    print("It is a tie! You both picked Scissors.")

else:
    print("You have to enter 0, 1, or 2!")