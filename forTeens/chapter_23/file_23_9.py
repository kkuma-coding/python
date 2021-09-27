import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.forward(50)
george.penup()          #Pull pen up
george.backward(200)
george.pendown()        #Pull pen down
george.forward(50) 

wn.exitonclick()
