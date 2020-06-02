import random

new_roll = ''

def roll():
	roll_result = random.randint(1,6)
	print(roll_result)
	

	


while True:
	roll()
	new_roll = input("Would you like to roll again? .\n (Y/N): ")
	if new_roll == 'Y' or new_roll == 'y':
		continue
		
	if new_roll == 'N' or new_roll == 'n':
		break
		
	else:
		print(new_roll)

print("Dice Roll has ended")

	
