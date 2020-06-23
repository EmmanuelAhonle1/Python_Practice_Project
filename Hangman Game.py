
"""
Name: Emmanuel Ahonle
Project: Hangman Game!

All the imports that I will be needing throughout this project
"""

#all the imports that I will be using throughout my project
import sys		#imports system sounds for mac
import time		#to measure time or delay functions
import random #picks random item froom list
import threading  #uses timer 


def animate(): #creates a loading animation where the slash spins clockwise
    for timer in range(0, 6):
        sys.stdout.write('\rYour game will begin shortly |')
        time.sleep(0.1)
        sys.stdout.write('\rYour game will begin shortly /')
        time.sleep(0.1)
        sys.stdout.write('\rYour game will begin shortly -')
        time.sleep(0.1)
        sys.stdout.write('\rYour game will begin shortly \\')
        time.sleep(0.1)
    sys.stdout.write('\r\n\n\n')

loop = 0
count = 0 #counts how many times incorrect input is typed into q1
word = ''      #randomly picked word from word_dictionary
split_chosen_word = [] #displays randomly chosen word's characters as items in list
tries_left = 0
position = 0
letter_bank = [] #empty list which is appended every time a user input is given

q1 = ''  #user input that determines difficulty
#all functions being used in Hangman game
	
	

#list of all nouns being used in Hangman Game
word_dictionary = [
    'people',
    'history',
    'way',
    'art',
    'world',
    'information',
    'map',
    'two',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power',
    'ability',
    'economics',
    'love',
    'internet',
    'television',
    'science',
    'library',
    'nature',
    'fact',
    'product',
    'idea',
    'temperature',
    'investment',
    'area',
    'society',
    'activity',
    'story',
    'industry',
    'media',
    'thing',
    'oven',
    'community',
    'definition',
    'safety',
    'quality',
    'development',
    'language',
    'management',
    'player',
    'variety',
    'video',
    'week',
    'security',
    'country',
    'exam',
    'movie',
    'organization',
    'equipment',
    'physics',
    'analysis',
    'policy',
    'series',
    'thought',
    'basis',
    'boyfriend',
    'direction',
    'strategy',
    'technology',
    'army',
    'camera',
    'freedom',
    'paper',
    'environment',
    'child',
    'instance',
    'month',
    'truth',
    'marketing',
    'university',
    'writing',
    'article',
    'department',
    'difference',
    'goal',
    'news',
    'audience',
    'fishing',
    'growth',
    'income',
    'marriage',
    'user',
    'combination',
    'failure',
    'meaning',
    'medicine',
    'philosophy',
    'teacher',
    'communication',
    'night',
    'chemistry',
    'disease',
    'disk',
    'energy',
    'nation',
    'road',
    'role',
    'soup',
    'advertising',
    'location',
    'success',
    'addition',
    'apartment',
    'education',
    'math',
    'moment',
    'painting',
    'politics',
    'attention',
    'decision',
    'event',
    'property',
    'shopping',
    'student',
    'wood',
    'competition',
    'distribution',
    'entertainment',
    'office',
    'population',
    'president',
    'unit',
    'category',
    'cigarette',
    'context',
    'introduction',
    'opportunity',
    'performance',
    'driver',
    'flight',
    'length',
    'magazine',
    'newspaper',
    'relationship',
    'teaching',
    'cell',
    'dealer',
    'debate',
    'finding',
    'lake',
    'member',
    'message',
    'phone',
    'scene',
    'appearance',
    'association',
    'concept',
    'customer',
    'death',
    'discussion',
    'housing',
    'inflation',
    'insurance',
    'mood',
    'woman',
    'advice',
    'blood',
    'effort',
    'expression',
    'importance',
    'opinion',
    'payment',
    'reality',
    'responsibility',
    'situation',
    'skill',
    'statement',
    'wealth',
    'application',
    'city',
    'county',
    'depth',
    'estate',
    'foundation',
    'grandmother',
    'heart',
    'perspective',
    'photo',
    'recipe',
    'studio',
    'topic',
    'collection',
    'depression',
    'imagination',
    'passion',
    'percentage',
    'resource',
    'setting',
    'ad',
    'agency',
    'college',
    'connection',
    'criticism',
    'debt',
    'description',
    'memory',
    'patience',
    'secretary',
    'solution',
    'administration',
    'aspect',
    'attitude',
    'director',
    'personality',
    'psychology',
    'recommendation',
    'response',
    'selection',
    'storage',
    'version']

def letters_in_word	(split_chosen_word, user_input):
	return split_chosen_word.count(user_input)
	

#randomly picks item from list to use as Hangman word	
word = random.choice(word_dictionary) #randomly picked word from word_dictionary
def turn_word_string_into_list(): #turns the randomly picked word from list into a string by splitting up the characters in the word
	for i in range(0, len(word)):
		split_chosen_word.append(word[i])
		i+=1

#Question 1: Determines how many failed attempts the player is given to guess the correct answer
print("Welcome to my Python Hangman Game! \nIn this game, you will be tasked with guessing the letters in a word. \n Depending on the chosen difficulty, you have more or less tries to finish the word. Good luck!")
time.sleep(3)

# chooses difficulty of game 
while True:
	time.sleep(.5)
	q1 = input('\nSelect a mode: \n \n [E]asy :) \n [M]edium :| \n [H]ard >:( \n Answer: ')
	print(q1)

		#enables easy mode: sets tries_left equal to 10; 10 allowed incorrect guesses
	if q1 in ['E', 'e']:
		time.sleep(.5)
		print("Ah a beginner I see! Don't worry, we'll give you ample time to  respond. You'll have 10 tries to type the correct answer \n")
		sys.stdout.write('\a')
		sys.stdout.flush()
		time.sleep(1)
		tries_left = 10
		break
		
#enables medium mode: sets tries_left equal to 5; 5 allowed incorrect guesses
	elif q1 in ['M', 'm']:
		time.sleep(.5)
		print("Ah so you're a bit experienced! You will be given 5 tries to type a response\n")
		sys.stdout.write('\a')
		sys.stdout.flush()
		tries_left = 5
		time.sleep(1)
		break
	
	#enables medium mode: sets tries_left equal to 3; 3 allowed incorrect guesses
	elif q1 in ['h', 'H']:
		time.sleep(.5)
		print("\nAh a daredevil I see! Let's see if you can put those skills to the test! You will be given 3 tries to guess the correct answer\n")
		sys.stdout.write('\a')
		sys.stdout.flush()
		tries_left = 3
		break
	
		#prints reply if correct answer isn't given
	else:
		count += 1
		if count >= 3:
			time.sleep(.5)
			print("Cmon now butterfingers I know you can type better than that. \n")
			
		else:
			print("that is not an answer. Please type carefully!")

turn_word_string_into_list()
guessed_word = []

#creates a list of '_' corresponding to the amount of items in the split_chosen_word list
for letters in range(0, len(split_chosen_word)):
	guessed_word.append('_')
	
	

#function checks if user's typed in letter matches list of chosen words and responds if you have already used this letter
def check_letter_bank():
	
	if letter_bank.count(user_input) >= 1:
		print("You have already used this letter.")
		time.sleep(.5)

		
		
correct = 0

print("**TIP** You can type in 'check' to check the letters you've already used")	
animate()	#calls animate function

print(word)
print(guessed_word)

while tries_left != 0: #conditions for if game is still continuing and there is not a game over
		
	while True:
			
		
		
			user_input = input('\nType in character OR guess the word: ')
			time.sleep(1)
			check_letter_bank()
			for position, letters in enumerate(split_chosen_word):
				if letters == user_input:
					guessed_word[position] = user_input
					#check_letter_bank()
					correct += 1

					
			
	
					
			#if the user guesses all the items in the list of characters from the random word, the code prints a message acknowledging correct word and exits terminal
			if guessed_word == split_chosen_word:
				print("\nCongrats! the word was '" + word + "'.")
				
				time.sleep(2)
				exit()
				
				
			#if the user guesses the word, code prints a message acknowledging correct guess and exits terminal
			elif user_input == word:
				print("Congrats!, the word was " + word)
				exit()
			
			elif user_input == 'check':
				print(letter_bank)
			
			#if user_input isn't found in list of the randomly picked word, then the program prints an error message and takes off a point in tries_left
			elif split_chosen_word.count(user_input) == 0:
				tries_left -= 1
				if user_input not in letter_bank:
					letter_bank.append(user_input)
				print("\nOof! Wrong answer! You have '" + str(tries_left) + "' tries left")
				
			
			if correct > 0:
				
				if user_input in letter_bank:
					break
					
				elif user_input == 'check':
					break
				else:
					letter_bank.append(user_input)
					correct = 0
					
			for position, letters in enumerate(split_chosen_word):
				if letters == user_input:		
					print("\nCongrats! '{}' occurs '{}' time(s)".format(user_input, letters_in_word(split_chosen_word, user_input)))
					break
			print(guessed_word)

		
		
		
		
		
		
		#if the player runs out of guessses, program prints 'Failed' message and the word that was meant to be guessed; exits terminal
			if tries_left == 0:
				print("\n \n \nPuzzle failed! Try again next time!")
				print("The word was '" + word + "'.'")
				time.sleep(5)
				exit()
	

