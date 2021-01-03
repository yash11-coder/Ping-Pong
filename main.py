
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time





timmy = Turtle()
timmy.color("black")
timmy.speed("fastest")

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

timmy.hideturtle()
timmy.penup()
timmy.goto(0,300)
for i in range(300,-300,-20):
   timmy.goto(0, i)
   timmy.pendown()
   timmy.goto(0, i+10)
   timmy.penup()
screen.tracer(0)



r_pad = Paddle((350,0),"red")
l_pad = Paddle((-350,0),"green")
ball = Ball()
screen.listen()
screen.onkey(l_pad.up, "W")
screen.onkey(l_pad.down, "S")
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")

score = Score()


game_is_on = True
while game_is_on ==True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 290 or ball.ycor()<-290:
        ball.bounce_y()


    if ball.xcor()>380:
        ball.move_speed = 0.1
        s2 = score.l_point()
        ball.reset_pos()

    if ball.xcor() < -380:
        ball.move_speed = 0.1
        s1 = score.r_point()
        ball.reset_pos()

    if ball.distance(r_pad) <50 and ball.xcor()>330:
        ball.move_speed *=0.9
        s1 = score.r_point()
        ball.bounce_x()

    if ball.distance(l_pad) <50 and ball.xcor()<-330:
        ball.move_speed *= 0.9
        s2 = score.l_point()
        ball.bounce_x()












screen.exitonclick()