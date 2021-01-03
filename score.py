from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-70,200)
        self.color("red")
        self.write(f"{self.l_score} ", align="center", font =("Arial", 50,"normal"))
        self.goto(100, 200)
        self.color("green")
        self.write(f"{self.r_score} ", align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()
