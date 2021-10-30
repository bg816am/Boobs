from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.speed("fast")
t.hideturtle()

t.pencolor("pink")
t.fillcolor("pink")
t.left(90)
t.begin_fill()
t.circle(100)
t.left(180)
t.circle(100)
t.end_fill()
t.penup()
t.left(90)
t.forward(100)
t.pencolor("brown")
t.dot(25)
t.left(180)
t.forward(200)
t.dot(25)

screen.exitonclick()

