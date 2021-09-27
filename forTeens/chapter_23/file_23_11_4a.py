import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.pensize(3)

for i in range(5):
    george.forward(150)
    george.right(180 / 5 * 4)     # 180 / 5 * 4 = 36 * 4 = 144 

wn.exitonclick()
