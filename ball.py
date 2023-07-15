import random
from turtle import Turtle

# Création de la balle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(45)
        self.x_step = 10
        self.y_step = 10
        self.speed_ball = 0.1

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1
        self.speed_ball *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed_ball = 0.1
        self.bounce_x()

