from turtle import *

#i is the number of times the turtle moves

#five squares
def fiveSquares():
	penup()
	goto(-350, 300)
	pendown()	
	pencolor("aquamarine2")
	for i in range (2):
		for i in range(4):
			side_length = 100
			forward(side_length)
			right(90)
			speed(1)
		penup()
		forward(130)	
		pendown()

#five triangles
def fiveTri():
	penup()
	goto(-350, 100)
	pendown()
	pencolor("blue violet")
	tri_length = 100
	for i in range (2):
		for i in range(3):
			forward(tri_length)
			left(120)
			speed(1)
		penup()
		forward(130)
		pendown()
	
#five circles
def fiveCircles():
	penup()
	goto(-300, -25)
	pendown()
	pencolor("coral")
	for i in range (2):
		speed(1)
		circle(50)
		penup()
		forward(120)
		pendown()


#five pentagons 
def fivePenta():
	penup()
	goto(-325, -75)
	pendown()
	pencolor("deep pink")
	for i in range (2):
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
	for i in range (2):
		for i in range(6):
			hexa_side = 50
			forward(hexa_side)
			right(60)
			speed(1)
		penup()
		forward(130)
		pendown()


fiveSquares()
fiveTri()
fiveCircles()
fivePenta()
fiveHexa()

