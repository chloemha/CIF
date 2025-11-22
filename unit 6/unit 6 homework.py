import turtle

turtle.shape("circle")
turtle.bgcolor("black")
turtle.color("white", "white")
turtle.pencolor("white")
turtle.speed(5)

turtle.penup()
turtle.goto(150,-150)
turtle.pendown()
turtle.fillcolor("yellow")

turtle.begin_fill()

for i in range(2):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.fillcolor("white")
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.left(90)
turtle.pencolor("white")
turtle.speed(10)

for a in range(50):
    turtle.forward(8)
    turtle.left(1)

turtle.speed(10)

turtle.penup()
turtle.forward(10)
turtle.pendown()

for d in range(8):
    turtle.forward(40)
    turtle.right(2)
    turtle.penup()
    turtle.backward(40)
    turtle.left(2)
    turtle.right(45)
    turtle.pendown()

turtle.done()