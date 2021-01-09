import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

for i in range(4):
    george.forward(50)
    george.left(90) 

wn.exitonclick()
