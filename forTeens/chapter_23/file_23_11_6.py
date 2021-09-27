import turtle

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.pensize(3)

flag = False
for x in range(18):
    george.forward(100)

    if flag == False:
        george.right(110)
    else:
        george.left(150)

    flag = not flag         #This statement reverses flag from True to False
                            #and vice versa

wn.exitonclick()
