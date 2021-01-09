import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

#Change pen's size to 5 pixels
george.pensize(5)

#Draw a thick line
george.backward(100)

#Change pen's size back to 1 pixel
george.pensize(1)

#Draw a thin line
george.backward(100) 

wn.exitonclick()
