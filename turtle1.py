import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
x = 1
y = 1
while True:
    if y < 50:
        alex.forward(x)
        alex.left(90)
        alex.forward(1)
        alex.left(90)
        alex.forward(x+1)
        alex.right(90)
        alex.forward(1)
        alex.right(90)
        x +=2
        y += 2
    elif y > 50 and y <100:
        alex.forward(x)
        alex.left(90)
        alex.forward(1)
        alex.left(90)
        alex.forward(x - 1)
        alex.right(90)
        alex.forward(1)
        alex.right(90)
        x -= 2
        y += 2
    else:
        break
wn.exitonclick()

