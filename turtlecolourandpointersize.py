import turtle
wincolor = input("Enter Window Colour: ")
pcolor = input("Enter Pointer Colour: ")
psize = int(input("Enter Pointer Size: "))
wn = turtle.Screen()
wn.bgcolor(wincolor)
tess = turtle.Turtle()
tess.color(pcolor)              # make tess blue
tess.pensize(psize)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
