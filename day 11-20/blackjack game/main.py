############### Blackjack Project #####################

############### Our Blackjack House Rules ####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random 
from art import logo
import os

def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def sum_cards(cards):

	if sum(cards) == 21 and len(cards) == 2:
		return 0

	if sum(cards) > 21 and 11 in cards:
		cards.remove(11)
		cards.append(1)
		
	return sum(cards)

def compare(player_score, computer_score):
	if player_score == computer_score:
		return "Draw"
	elif  computer_score == 0:
		return "Bust! Opponent has BlackJack!"
	elif player_score == 0:
		return "Win! You have a BlackJack!"
	elif player_score > 21:
		return "Bust! You went over. You lose!"
	elif computer_score > 21:
		return "Opponent Bust! You win!"
	elif player_score > computer_score:
		return "You Win!"
	else:
		return "You lose!"

def play_game():
	print(logo)
	
	player_cards = []
	computer_cards = []
	is_game_over = False
	
	for i in range(2):
		player_cards.append(deal_card())
		computer_cards.append(deal_card())
	
	while not is_game_over:
		player_score = sum_cards(player_cards)
		computer_score = sum_cards(computer_cards)
		print(f"Your cards: {player_cards}, current score: {player_score}")
		print(f"Computer's first card: {computer_cards[0]}")
		
		if player_score == 0 or computer_score == 0 or player_score > 21:
			is_game_over = True
		else:
			player_choice = input("Do you want to stand(no new card) or hit(deal a new card)? Type 'y' or 'n' to continue: ")
			if player_choice == 'y':
				player_cards.append(deal_card())
			else:
				is_game_over = True
		
	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = sum_cards(computer_cards)
		
	print(f"   Your final hand: {player_cards}, final score: {player_score}")
	print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")	
	
	print(compare(player_score, computer_score))
	
while input("Welcome to the BlackJack game.\nDo you want to play the game? 'y' to start, 'n' if otherwise: ") == "y":
	os.system('cls')
	play_game()




