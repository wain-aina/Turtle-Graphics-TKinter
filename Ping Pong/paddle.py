from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)

    def go_up(self):
        self.new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), self.new_y)
