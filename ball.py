from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        p = self.xcor() + self.x_move
        q = self.ycor() + self.y_move
        self.goto(p, q)

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()



