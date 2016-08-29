import turtle
g = 134
l = 120
iterations = (int)(input("Please enter the number of iterations you'd like to see: "))
while iterations > 0:
    turtle.left(g)
    turtle.forward(l)
    iterations -= 1