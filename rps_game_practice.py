# ~ def f(): 
	# ~ print(s)

	# ~ # This program will NOT show error 
	# ~ # if we comment below line. 
	# ~ s = "Me too."

	# ~ print(s) 

# ~ # Global scope 
# ~ s = "I love Geeksforgeeks"
# ~ f() 
# ~ print(s)


# This function has a variable with 
# name same as s. 
def f(): 
	s = "Me too."
	print(s)

# Global scope 
s = "I love Geeksforgeeks"
f() 
print(s)

