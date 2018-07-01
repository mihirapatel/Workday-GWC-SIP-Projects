from turtle import *

#i is the number of times the turtle moves

#five squares

def fiveSquares(xCor, yCor,shapeColor, sideLength):
	penup()
	goto(xCor, yCor)
	pendown()	
	pencolor(shapeColor)
	for i in range (5):
		for i in range(4):
			forward(sideLength)
			right(90)
			speed(1)
		penup()
		forward(130)	
		pendown()

#five triangles
# def fiveTri():
# 	penup()
# 	goto(-350, 100)
# 	pendown()
# 	pencolor("blue violet")
# 	tri_length = 100
# 	for i in range (2):
# 		for i in range(3):
# 			forward(tri_length)
# 			left(120)
# 			speed(1)
# 		penup()
# 		forward(130)
# 		pendown()
	
#five circles
# def fiveCircles():
# 	penup()
# 	goto(-300, -25)
# 	pendown()
# 	pencolor("coral")
# 	for i in range (5):
# 		speed(1)
# 		circle(50)
# 		penup()
# 		forward(140)
# 		pendown()



# penup()
# goto(-200, 100)
# pendown()
# pencolor("deep pink")
# 
# penta_side = 75
# for i in range(5):
# 	forward(penta_side)
# 	right(72)
# 	speed(1)

# 
# penup()
# goto(-100, 200)
# pendown()
# pencolor("255, 204, 229") 

# 
# hexa_side = 50
# for i in range(6):
# 	forward(hexa_side)
# 	right(60)
# 	speed(1)


fiveSquares(-350, 300, "aquamarine2", 100)
fiveSquares(-350, 100, "red", 50)
fiveTri()
fiveCircles()
