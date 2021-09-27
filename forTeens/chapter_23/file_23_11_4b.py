import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.pensize(3)

points = 7

for i in range(points):
    george.forward(150)
    george.right(180 / points * (points - 1)) 

wn.exitonclick()
