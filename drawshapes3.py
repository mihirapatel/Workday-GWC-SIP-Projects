from turtle import *

#i is the number of times the turtle moves

#PART ONE AND TWO (OF PART 3)

#five squares
def fiveSquares(xCor, yCor, squareColor, sideLength):
	penup()
	goto(xCor, yCor)
	pendown()	
	pencolor(squareColor)
	for i in range (5):
		for i in range(4):
			forward(sideLength)
			right(90)
			speed(1)
		penup()
		forward(130)	
		pendown()
		
#five triangles
def fiveTri(xCor, yCor, triColor, triLength):
	penup()
	goto(xCor, yCor)
	pendown()
	pencolor(triColor)
	for i in range (5):
		for i in range(3):
			forward(triLength)
			left(120)
			speed(1)
		penup()
		forward(130)
		pendown()
	
# five circles
def fiveCircles():
	penup()
	goto(-300, -25)
	pendown()
	pencolor("coral")
	for i in range (5):
		speed(1)
		circle(50)
		penup()
		forward(120)
		pendown()


# five pentagons 
def fivePenta():
	penup()
	goto(-325, -75)
	pendown()
	pencolor("deep pink")
	for i in range (5):
		for i in range(5):
			penta_side = 65
			forward(penta_side)
			right(72)
			speed(1)
		penup()
		forward(130)
		pendown()

# five hexagons
def fiveHexa():
	penup()
	goto(-325, -200)
	pendown()
	pencolor("green") 
	for i in range (5):
		for i in range(6):
			hexa_side = 50
			forward(hexa_side)
			right(60)
			speed(1)
		penup()
		forward(130)
		pendown()



# fiveSquares(-350, 300, "aquamarine2", 100)
# fiveSquares(-350, 250, "red", 50)
# fiveTri(-350, 0, "blue violet", 100)
# fiveTri(-350, -100, "green", 50) 
# fiveCircles()
# fivePenta()
# fiveHexa()

#PART THREE (OF PART THREE)

#five squares
def fiveSquares(xCor, yCor, squareColor, sideLength):
	penup()
	goto(xCor, yCor)
	pendown()	
	pencolor(squareColor)
	for i in range(4):
		forward(sideLength)
		right(90)
		speed(1)
	
#five triangles
def fiveTri(xCor, yCor, triColor, triLength):
	penup()
	goto(xCor, yCor)
	pendown()
	pencolor(triColor)
	for i in range(3):
		forward(triLength)
		left(120)
		speed(1)

# fiveSquares(-350, 300, "aquamarine2", 50)
# fiveSquares(-290, 300, "blue violet", 50)
# fiveSquares(-230, 300, "coral", 50)
# fiveTri(-350, 200, "aquamarine2", 50)
# fiveTri(-290, 200, "blue violet", 50)
# fiveTri(-230, 200, "coral", 50)

# PART FOUR (OF PART THREE)
#asks the user how many sides it wants the shape to have and which color

userSides = input("How many sides do you want on your shape?: ")
userColor = input("Which color do you want to make the shape?: ")

def drawShape(userColor):
	for i in range (int(userSides)):
		pencolor(userColor) 
		pendown()
		shapeSide = 100
		forward(shapeSide)
		right(360/ int(userSides))
		speed(1)	
#drawShape(userColor)

# PART FIVE (OF PART THREE)

def drawPoly(xCor, yCor):
    goto(xCor, yCor)
    regular_polygon(5, 20, “maroon”)


drawPoly(-350, 0)



































