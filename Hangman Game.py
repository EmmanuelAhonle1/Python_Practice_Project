
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


loop = 0
count = 0
word = ''
split_chosen_word = []
tries_left = 0
position = 0
letter_bank = []

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
	
	
word = random.choice(word_dictionary)
def turn_word_string_into_list():
	for i in range(0, len(word)):
		split_chosen_word.append(word[i])
		i+=1

#Question 1: Determines how long the words will be
print("Welcome to my Python Hangman Game! \nIn this game, you will be tasked with guessing the letters in a word. \n Depending on the chosen difficulty, you have more or less tries to finish the word. Good luck!")
time.sleep(3)

# chooses difficulty of game 
while True:
	time.sleep(.5)
	q1 = input('\nSelect a mode: \n \n [E]asy :) \n [M]edium :| \n [H]ard >:( \n Answer: ')
	print(q1)

		#enables easy mode: no timer 
	if q1 in ['E', 'e']:
		time.sleep(.5)
		print("Ah a beginner I see! Don't worry, we'll give you ample time to  respond. You'll have 10 tries to type the correct answer \n")
		sys.stdout.write('\a')
		sys.stdout.flush()
		time.sleep(1)
		tries_left = 10
		break
		
#enables medium mode: 15 second timer
	elif q1 in ['M', 'm']:
		time.sleep(.5)
		print("Ah so you're a bit experienced! You will be given 5 tries to type a response\n")
		sys.stdout.write('\a')
		sys.stdout.flush()
		tries_left = 5
		time.sleep(1)
		break
	
	#enables medium mode: 15 second timer
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

for letters in range(0, len(split_chosen_word)):
	guessed_word.append('_')
	
	


def check_letter_bank():
	if user_input in letter_bank:
		print("You have already used this letter.")
		
		
print("\n\n\nThe game will start shortly")
time.sleep(3)
print(guessed_word)

while tries_left != 0:
		
	while True:
			user_input = input('\nType in character OR guess the word: ')
			time.sleep(1)
			for position, letters in enumerate(split_chosen_word):
				if letters == user_input:
					guessed_word[position] = user_input
					print("\nCongrats! '{}' occurs '{}' time(s)".format(user_input, letters_in_word(split_chosen_word, user_input)))
					check_letter_bank()
					letter_bank.append(user_input)
					print(guessed_word)
					
			if guessed_word == split_chosen_word:
				print("\nCongrats! the word was '" + word + "'.")
				
				time.sleep(2)
				exit()
			
			elif user_input == word:
				print("Congrats!, the word was " + word)
				exit()
			
			elif split_chosen_word.count(user_input) == 0:
				tries_left -= 1
				print("\nOof! Wrong answer! You have '" + str(tries_left) + "' tries left")
				print(guessed_word)
			
		
		
		
		
		
		
		
		
		
		
			if tries_left == 0:
				print("\n \n \nPuzzle failed! Try again next time!")
				print("The word was '" + word + "'.'")
				time.sleep(5)
				exit()
	

