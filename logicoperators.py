my_number = 52	

def guessnumber():

	user_number = input ("Guess my number: ")

	if int(user_number) == my_number:
		print("Good job! You guess the right number")
		print("Game over")
	elif int(user_number) > my_number:
		print("You number is too high")
		guessnumber()
	else:
		print("Your number is too low")
		guessnumber()

guessnumber()
	
