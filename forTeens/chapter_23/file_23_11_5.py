import random
import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Draw stars as quickly as possible
turtle.delay(0)

for star in range(10):
    #Pick random x, y values and move the turtle to that position
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    george.penup()
    george.goto(x, y)
    george.pendown()

    #Pick a random number of points
    points = random.randrange(5, 23, 2) 

    #Pick a random side length
    length = random.randrange(10, 100)

    #Draw a star
    for i in range(points):
        george.forward(length)
        george.right(180 / points * (points - 1)) 

wn.exitonclick()
