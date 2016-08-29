import turtle

class ChangeColor:
    def change_color(self, color):
        if(color % 2 == 0):
            turtle.color('black')
        else:
            turtle.color('white')
color = ChangeColor()

length = 50
turtle.speed('fastest')
#get a better starting position
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

for k in range (8):
    if(k % 2 == 0): #foward
        for i in range(8): #draw a row
            color.change_color(i)
            turtle.begin_fill()
            for j in range (4): #draw a cell
                turtle.forward(length)
                turtle.left(90)
            turtle.end_fill()
            turtle.forward(length)
        turtle.left(90) #point upward
        turtle.forward(length*2) #go upward to the next row
        turtle.right(90) #point the turtle back to the right
    else: #backward
        for i in range(8): #draw a row
            color.change_color(i)
            turtle.begin_fill()
            for j in range (4): #draw a cell
                turtle.backward(length)
                turtle.left(90)
            turtle.end_fill()
            turtle.backward(length)
#draw borders
turtle.goto(-200,-200)
turtle.color('black')
for i in range(4):
    turtle.forward(8*length)
    turtle.left(90)

turtle.exitonclick()



