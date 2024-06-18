import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")

t = Turtle()
t.reset()
t.speed(0)

turtle.colormode(255)

a=0
b=0

def random_color(x):
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

while b < 100:
    test = int(a)
    color = random_color(test)
    turtle.color(color)
    turtle.forward(b)
    turtle.right(150)

    b = b + 0.6
    a = a + 0.5

screen.exitonclick()


