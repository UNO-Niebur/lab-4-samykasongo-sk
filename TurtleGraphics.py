#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(sam, sides):
    for k in range(sides):
        sam.forward(75)
        sam.right(360/8)
        
def fillCorner(kasongo, corner):
    #draw big squre
    drawSquare(kasongo, 150)
    
    if corner == 1:
        kasongo.bigin_fill()
        drawSquare (kasongo, 75)
        kasongo.end_fill()
        
    elif corner == 2:
        kasongo.forward(75)
        kasongo. begin_fill()
        drawSquare(kasongo, 75)
        kasongo.end_fill()
        
    elif corner == 3:
        kasongo.left(75)
        kasongo.right(75)
        kasongo.begin_fill()
        drawSquare(kasongo, 75)
        kasongo.end_fill()
        
def squaresInSquares(ben, num):

    # starting size == 200 (1)
    
    for k in range (num):
        # draw one square
        ben.pendown()
        ben.forward (200)
        ben.right(90) 
        
    # move to new startn(centered)
    ben.pendown()
    ben.forward(20/2)
    ben.right(90)
    ben.forward(20/2)
    ben.left(90)
    ben.pendown()
    
     # starting size == 180 (2)
     
    for k in range (num):
        # draw one square
        ben.pendown()
        ben.forward (180)
        ben.right(90) 
        
    # move to new startn(centered) 
    ben.penup()
    ben.forward(20/2)
    ben.right(90)
    ben.forward(20/2)
    ben.left(90)
    ben.pendown()
    
    # starting size == 160 (3)
     
    for k in range (num):
        # draw one square
        ben.pendown()
        ben.forward (160)
        ben.right(90) 
        
    # move to new startn(centered) 
    ben.penup()
    ben.forward(20/2)
    ben.right(90)
    ben.forward(20/2)
    ben.left(90)
    ben.pendown()
    
    # starting size == 130 (4)
     
    for k in range (num):
        # draw one square
        ben.pendown()
        ben.forward (130)
        ben.right(90) 
        
    # move inside for next square 
    ben.penup()
    ben.forward(20/2)
    ben.right(90)
    ben.forward(20/2)
    ben.left(90)
    ben.pendown()
    
    # starting size == 100 (5)
     
    for k in range (num):
        # draw one square
        ben.pendown()
        ben.forward (100)
        ben.right(90) 
        
    # move inside for next square 
    ben.penup()
    ben.forward(20/2)
    ben.right(90)
    ben.forward(20/2)
    ben.left(90)
    ben.pendown()
    
    
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle,150)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

main()
