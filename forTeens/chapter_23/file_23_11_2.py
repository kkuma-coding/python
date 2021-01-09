import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Move the turtle to pole position
george.penup()
george.backward(330)
george.pendown()

for multiplier in range(1, 4):
    #Draw a rectangle
    george.forward(100 * multiplier)
    george.left(90)
    george.forward(50 * multiplier)
    george.left(90)
    george.forward(100 * multiplier)
    george.left(90)
    george.forward(50 * multiplier)

    #Move George to the top left corner of the rectangle
    george.penup()
    george.backward(50 * multiplier)
    george.pendown()

    #Draw the roof
    george.setheading(45)
    george.forward(70.5 * multiplier)
    george.right(90)
    george.forward(70.5 * multiplier)

    #Move george to a position
    #where next house will be drawn
    george.penup()
    george.setheading(270)
    george.forward(50 * multiplier)
    george.setheading(0)
    george.forward(30)
    george.pendown()

wn.exitonclick()
