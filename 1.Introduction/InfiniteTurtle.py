import turtle

while True:
    angle = (int)(input("Please input the angle at which you'd like the turtle to turn"))
    length = (int)(input("Please input the length at which you'd like the turtle to move forward"))
    turtle.left(angle)
    turtle.forward(length)


