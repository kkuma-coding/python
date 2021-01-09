import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Set the delay to 50 milliseconds
turtle.delay(50)

#Draw a triangle
george.forward(100)
george.left(120)
george.forward(100)
george.left(120)
george.forward(100)
george.left(120) 

wn.exitonclick()
