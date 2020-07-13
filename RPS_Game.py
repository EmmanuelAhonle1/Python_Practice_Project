"""
Name: Emmanuel Ahonle

Project: Rock, Paper, Scissors Game

Date Created: June 23, 2020

Date Modified: 
"""


import random
import time
from stringcolor import * 


cpu_choice_list = ['Rock', 'Paper', 'Scissors']
player_wins = 0
cpu_wins = 0

player_choice = ''
play_again = ''
cpu_choice = ''

def play_again_prompt():
	
	global play_again
	global cpu_wins
	global player_wins
	
	
	
	cpu_wins = 0
	player_wins = 0
	play_again = input(f'Would you like to play again?(Y/N):')
	
	
	#ASSERTION to check if player input didn't process or was left blank to play the RPS Game again
	assert len(play_again) != 0, 'User did not type in value'
	
	time.sleep(2)
	if play_again in ['Y', 'y']:
		print('SCORES HAVE BEEN RESET')
		time.sleep(3)
		play_game()
		
	elif play_again in ['N', 'n']:
		print(f'Thanks for playing! Hope you enjoyed it!')
		time.sleep(1)
		exit()
		
	else:
		print(f'Please type an acceptable response.\n\n')
		play_again_prompt()

def check_winner():
	
	global player_wins
	global cpu_wins
	global player_wins
	
	
	if player_wins == 2:
		print(f'Player Wins; good job!\n')
		play_again_prompt()

	
	elif cpu_wins == 2:
		print(f'Computer Wins; better luck next time!\n')
		play_again_prompt()
		
		
		
def player_chooses_paper(player_choice, cpu_choice, cpu_wins, player_wins):
	
	
	if player_choice.title() == 'Paper':
		
		if cpu_choice == 'Rock':
			print(f'Player wins round! Paper covers Rock\n\n')
			player_wins += 1
		
		elif cpu_choice == player_choice.title():
			print(f'Tie!')
			
		else:
			print(f'Computer wins round! Scissors cut Paper\n\n')
			cpu_wins += 1
			
def player_chooses_rock():
	
	global player_choice
	global cpu_choice
	global cpu_wins
	global player_wins
	
	if player_choice.title() == 'Rock':
		
		if cpu_choice == 'Scissors':
			print(f'Player wins round! Rock smashes Scissors\n\n')
			player_wins += 1
		
		elif cpu_choice == player_choice.title():
			print(f'Tie!')
			
		else:
			print(f'Computer wins round! Paper covers Rock\n\n')
			cpu_wins += 1
			
			
def player_chooses_scissors():
	
	global player_choice
	global cpu_choice
	global cpu_wins
	global player_wins
	
	
	if player_choice.title() == 'Scissors':
		
		if cpu_choice == 'Paper':
			print(f'Player wins round! Scissors cuts Paper\n\n')
			player_wins += 1
		
		elif cpu_choice == player_choice:
			print(f'Tie!')
			
		else:
			print(f'Computer wins round! Rock smashes Scissors\n\n')
			cpu_wins += 1
	
		
			
			

		
	
	







	
print(f"Hi!, This is a Rock, Paper, Scissors Simulator. This will be a 'best-of-three' game so either the computer or player must win 2 times. Have fun! This program is not uppercase sensitive so don't be worried about capitalization\n\n")
	
#time.sleep(8)

def play_game():

	global player_choice
	global cpu_choice
	global cpu_wins
	global player_wins
	global player_wins
	global cpu_wins
	global player_wins

	while player_wins != 2 or cpu_wins != 2: 
			
		check_winner()
		cpu_choice = random.choice(cpu_choice_list)
		player_choice = input(f"\n\nType 'Rock', 'Paper', or 'Scissors':   ").title()
		
		if player_choice not in cpu_choice_list:
			print('Please type an acceptable response')

			
		time.sleep(1)
		
		player_chooses_paper()
				
		player_chooses_rock()
				
		player_chooses_scissors()
		
		print('\n')
		print(bold(f"Player wins: {player_wins}  |   CPU wins: {cpu_wins}").cs("red", "gold"))

	
#play_game()
	
	
#player_choice, cpu_choice, cpu_wins, player_wins

def test_player_chooses_paper():
	player_choice = 'Paper'
	cpu_choice = 'Rock'
	cpu_wins = 0
	player_wins = 0
	
	player_chooses_paper(player_choice, cpu_choice, cpu_wins, player_wins)
	assert player_wins == 1
