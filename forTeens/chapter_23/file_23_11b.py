import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Move the turtle to pole position
george.penup()
george.backward(200)
george.pendown()

for square in range(2):
    #Draw a square
    for i in range(4):
        george.forward(50)
        george.left(90)

    #Move the turtle to the position
    #where next square will be drawn
    george.penup()
    george.forward(100)
    george.pendown()

wn.exitonclick()
