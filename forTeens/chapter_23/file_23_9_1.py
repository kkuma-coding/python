import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Draw a blue rectangle
george.color("blue")
george.forward(200)
george.left(90)
george.forward(100)
george.left(90)
george.forward(200)
george.left(90)
george.forward(100)

#Move George to the top left corner of the rectangle
george.penup()
george.backward(100)
george.pendown()

#Draw the red roof
george.setheading(45)
george.color("red")
george.forward(141)
george.right(90)
george.forward(141) 

wn.exitonclick()
