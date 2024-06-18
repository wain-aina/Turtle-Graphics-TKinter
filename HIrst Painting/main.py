import turtle
from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
turtle.colormode(255)

timmy.shape("turtle")
timmy.speed(0)

# def random_colours():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)

# directions = [0, 90, 180, 270]
#
# def random_move(num_times):
#     for i in range(num_times):
#         timmy.color(random_colours())
#         timmy.forward(30)
#         timmy.right(random.choice(directions))

# random_move(1000)

# def spiro(num_of_circles):
#     for i in range(num_of_circles):
#         radius = 125
#         angle = 360/num_of_circles
#         timmy.color(random_colours())
#         timmy.circle(radius)
#         timmy.right(angle)
#
# spiro(100)

rgb_colors = []
colors = colorgram.extract("spot.jpg", 24)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

color_list = [(237, 34, 109), (153, 24, 65), (240, 73, 34), (7, 147, 92), (218, 170, 46), (179, 158, 44), (25, 123, 190), (44, 190, 232), (83, 20, 77), (244, 220, 47), (252, 223, 1), (125, 192, 84), (183, 39, 104), (207, 63, 24), (56, 172, 103), (170, 24, 19), (205, 133, 166), (4, 106, 45), (27, 176, 211), (237, 163, 193)]

def hirst_painting(space, matrix):
    for i in range(10):
        for x in range(10):
            timmy.dot(20, random.choice(color_list))
            timmy.forward(space)
            timmy.dot(20)
        timmy.backward(space * matrix)
        timmy.left(90)
        timmy.forward(space)
        timmy.right(90)

timmy.penup()
hirst_painting(30, 10)



screen = Screen()
screen.exitonclick()