import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.pensize(2)

sides = 5

for i in range(sides):
    george.forward(100)
    george.right(360 / sides) 

wn.exitonclick()
