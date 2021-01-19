import turtle
import random
colorlist = ["aqua","black","brown","blue","coral","forestgreen","indigo","lightskyblue","lightsalmon","lightseagreen","lightslategray","lime","navy","olive","orangered","yellow","red"]
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(12)
alex.speed(0)
a = 3.0
alex.up()
alex.right(90)
alex.forward(180)
alex.left(90)
alex.down()
for i in range(15):
    randomclr = random.choice(colorlist)
    alex.color(randomclr)
    colorlist.remove(randomclr)
    b = list(alex.pos())
    b[0] = int(b[0])
    b[1] = int(b[1])
    print(b)
    while True:
        alex.left(1)
        alex.forward(a)
        c = list(alex.pos())
        c[0] = int(c[0])
        c[1] = int(c[1])
        if c == b:
            break
    # if i%2 == 0:
    alex.up()
    alex.left(90)
    alex.forward(12)
    alex.right(90)
    alex.down()
    a =  a - 0.2
wn.exitonclick()

