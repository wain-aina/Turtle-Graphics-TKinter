from turtle import Turtle, Screen

screen = Screen()
v = Turtle()

v.speed(0)

def curve():
    for i in range(200):
        v.right(i)
        v.forward(i)

def rona():
    v.left(140)
    curve()

def txt():
    v.penup()
    v.setpos(50, -250)
    v.pendown()
    v.color("red")
    v.write("LIES", align='center', font=("Maiden Orange", 30, "bold"))
    v.hideturtle()

rona()
txt()

screen.exitonclick()