import random
from art import logo
print(logo)

def difficulty():
	game_level = input("What game difficulty do you want? Type 'easy', 'medium', or 'hard': ")
	if game_level == "easy":
		turns = 10
	elif game_level == "medium":
		turns = 7
	else:
		turns = 5
	return turns

def check(guess, correct_number, turns):
	if guess < 1 or guess > 100:
		print("Out of range")
	if guess == correct_number:
		print(f"You guessed {guess}. This is the correct number.")
	elif guess < correct_number:
		print ("You guessed too low.")
		return turns - 1
	elif guess > correct_number:
		print ("You guessed too high.")
		return turns - 1
		
def game():
	print("Welcome to the Number Guessing Game!")
	correct_number = random.randint(1,101)
	turns = difficulty()
	
	guess = 0
	while guess != correct_number:
		print(f"You have {turns} attempts left.")
		guess = int(input("Guess a number between 1 and 100: "))
		turns = check(guess, correct_number, turns)
		if turns == 0:
			print("You have run out of guesses, you lose!")
			print(f"The correct number is {correct_number}")
			return 
		elif guess != correct_number:
			print("Guess again.")
		
	
game()