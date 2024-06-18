from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            self.new_car = Turtle()
            self.new_car.shape("square")
            self.new_car.shapesize(1, 2)
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            self.new_car.goto(300, random_y)
            self.all_cars.append(self.new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
