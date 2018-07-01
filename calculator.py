myCalculator = True

# def myCalculator():
while myCalculator:

    userOp = input("What operation do you want to carry out? 'add', 'substract', 'divide', 'multiply', 'exponent': ")
    userNumOne = input("Type in your first number: ")
    userNumTwo = input("Type in your second number: ")

    if userOp == "add":
        answer = int(userNumOne) + int(userNumTwo)
        print(answer)
    elif userOp == "subtract":
        answer = int(userNumOne) - int(userNumTwo)
        print(answer)
    elif userOp == "divide":
        answer = int(userNumOne) / int(userNumTwo)
        print(answer)
    elif userOp == "exponent":
        answer = int(userNumOne) ** int(userNumTwo)
        print(answer)
    elif userOp == "multiply":
        answer = int(userNumOne) * int(userNumTwo)
        print(answer)
    else:
        myCalculator = False

ifdone = input("Are you done? 'yes' or 'no': ")
if ifdone == "yes":
    myCalculator = True
else:
    myCalculator = False

# myCalculator()
