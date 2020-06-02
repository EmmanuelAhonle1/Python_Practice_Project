
while True:
	x = input("Enter possible palindrome: ")


	if x == x[::-1]:
		print(True)

	else:
		print(False)
