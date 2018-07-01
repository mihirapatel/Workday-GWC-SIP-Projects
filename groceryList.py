
"""

user_input = input("List a grocery item: ")

keepGoing = "y"

while keepGoing == "y":
	groceryList = [user_input]
	print(groceryList)

	keepGoing = input("Do you want to continue? Type 'y' or 'n'")

	if keepGoing == "y":
		user_input += ", " + input("List a grocery item: ") 

	else:
		keepGoing == "n"

		"""
from turtle import *		
penup()		
goto(250,350)
pencolor("yellow")
pendown()
circle(100)
speed(1)