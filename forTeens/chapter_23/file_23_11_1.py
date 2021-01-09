import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Move the turtle to pole position
george.penup()
george.backward(330)
george.pendown()

for multiplier in range(1, 4):    
    #Draw a square
    for i in range(4):
        george.forward(50 * multiplier)
        george.left(90)

    #Move george to a position
    #where next square will be drawn
    george.penup()
    george.forward(50 * multiplier)
    george.forward(30)
    george.pendown()

wn.exitonclick()
