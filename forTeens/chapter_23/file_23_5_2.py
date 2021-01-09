import turtle

x = int(input("Enter the length of the base: "))
y = int(input("Enter the length of the height: "))

wn = turtle.Screen()
george = turtle.Turtle()
george.shape("turtle")

george.forward(x)
george.left(90)
george.forward(y)
george.left(90)
george.forward(x)
george.left(90)
george.forward(y) 

wn.exitonclick()
