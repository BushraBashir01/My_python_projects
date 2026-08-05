import turtle

turtle.color("blue")
turtle.penup()
turtle.goto(-34,-89)
turtle.pendown()
turtle.circle(50)



turtle.color("green")
turtle.penup()
turtle.goto(-87,-76)
turtle.pendown()
turtle.circle(100)



for i in range(2):
    turtle.color("yellow")
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)

for i in range(4):
    turtle.color("red")
    turtle.forward(100)
    turtle.right(90)


turtle.done()

