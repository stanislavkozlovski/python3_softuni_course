import turtle
i = 10
distanceTraveled = 0

while i < 61:
    if(distanceTraveled == 100):
        for iterator in range(15):
            turtle.right(iterator)
            turtle.forward(iterator)
    if(i % 2 == 0):
        turtle.right(100)
        turtle.forward(30)
        distanceTraveled += 30
        turtle.color('red')
        turtle.speed('slow')

    if (i == 30):
        turtle.color('orange')
    turtle.left(i % 48)
    turtle.forward(10)
    distanceTraveled += 10
    i+=1