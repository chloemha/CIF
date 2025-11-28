#importing turtle function
import turtle

#setting up the turtle appearance
turtle.shape("circle")
turtle.bgcolor("black")
turtle.color("white", "white")
turtle.pencolor("white")
turtle.speed(5)

#setting up the location
turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.fillcolor("red")

#starting to colour in the firework box
turtle.begin_fill()

#making the firework box
for i in range(2):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

#setting up the new things for the actual firework
turtle.fillcolor("white")
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.left(90)
turtle.pencolor("white")
turtle.speed(10)

#the long line that leads to the firework
for i in range(50):
    turtle.forward(8)
    turtle.left(1)

#changing the speed
turtle.speed(10)

#making the direction of the firework
turtle.penup()
turtle.forward(10)
turtle.pendown()

#firework colour
turtle.color("yellow")
turtle.pencolor("yellow")

#a bigger firework size
size=1
for i in range(5):
    size+=0.2
    turtle.shapesize(size)

#speed of the bloom of the fireworks
turtles=[]*36
print("Here")
turtle.delay(0)
turtle.speed(0)

#the actual bloom of the fireworks
for i in range(36):
    turtles.append(turtle.clone())
    turtles[i].speed(0)
    turtles[i].right(i*20)
    turtles[i].color("yellow")
    turtles[i].shapesize(0.1)
    turtles[i].pencolor("yellow")

#the blooming pattern
for j in range(200):
    for i in range(36):
        turtles[i].forward(50)
        turtles[i].left(40)

print("done")

turtle.done()