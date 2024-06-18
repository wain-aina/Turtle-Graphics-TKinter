import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect player has reached other side
    if player.ycor() > 280:
        player.restart()
        score.increase_score()
        cars.increase_speed()


screen.exitonclick()