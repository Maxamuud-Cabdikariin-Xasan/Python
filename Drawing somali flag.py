import turtle
NO_LINES = 5
turtle.showturtle()
turtle.fillcolor("azure")
turtle.begin_fill()
turtle.pensize(5)
turtle.pencolor('blue')
turtle.fillcolor("blue")
turtle.begin_fill()
# drawing rectangle
for s in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()
turtle.setheading(270)
turtle.forward(300)
turtle.end_fill()
turtle.penup()
turtle.backward(450)
turtle.setheading(0)
turtle.forward(100)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor('white')
turtle.fillcolor('white')
turtle.begin_fill()
# drawing star
for m in range(NO_LINES):
    turtle.left(-72)
    turtle.forward(100)
    turtle.right(72)
turtle.end_fill()
turtle.hideturtle()

turtle.done()