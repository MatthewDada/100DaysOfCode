from game_data import data
from art import logo, vs
import random
import os

def random_option():
	return data[random.randint(0, len(data)-1)]

def format_data(account):
	name = account["name"]
	description = account["description"]
	country = account["country"]
	return f"{name}, a {description}, from {country}"

def compare_followers(followers_A, followers_B, user_input):
	global grade
	if followers_A > followers_B and user_input == "A" or followers_B > followers_A and user_input == "B":
		grade = "correct"
	elif followers_A > followers_B and user_input == "B" or followers_B > followers_A and user_input == "A":
		grade = "wrong"

	return grade

def game():
	print(logo)
	score = 0
	game_on = True
	account_b = random_option()
	
	while game_on:
		account_a = account_b
		account_b = random_option()

		while account_a == account_b:
			account_b = option_B
		
		print(f"Compare A: {format_data(account_a)}.")
		print(vs)
		print(f"Against B: {format_data(account_b)}.")

		follower_count_A = account_a["follower_count"]
		follower_count_B = account_b["follower_count"]

		user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

		os.system('cls')
		print(logo)

		if compare_followers(follower_count_A, follower_count_B, user_input) == 'correct':
			score += 1
			print(f"you're right! Current score: {score}.")
		else:
			game_on = False
			print(f"Sorry, that's wrong. Final score: {score}")

game()