import turtle

turtle.color("green")
turtle.pencolor("green")

side=int(input("Please enter the number of sides you want for your polygon"))
length=int(input("Please enter the length you want for each side"))

for i in range(side):
    turtle.forward(length)
    turtle.right((side-2)*180/side)

turtle.done()