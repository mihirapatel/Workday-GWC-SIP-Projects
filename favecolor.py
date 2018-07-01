my_color = "blue"
guess = input("What is my favorite color? ")
while guess != my_color:
	guess = input("What is my favorite color? ")
while guess == my_color:
	print("Good job, you guess correctly")
	my_color = False 
