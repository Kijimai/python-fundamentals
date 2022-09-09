# Create The screen
# Create and Move the paddle
# Create another paddle (Computer)
# Detect Collision with wall and bounce
# Detect Collision with paddle
# Create score for each player
# Detect when paddle misses and hits behind opposite player's paddle
from pong_ball import PongBall
from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
import time
game_started = True

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Extreme Ping Pong")
screen.listen()
screen.tracer(0)
score = ScoreBoard()

ball = PongBall()

p1_paddle = Paddle((-380, 0))
p2_paddle = Paddle((380, 0))

screen.onkeypress(p1_paddle.move_up, "w")
screen.onkeypress(p1_paddle.move_down, "s")
screen.onkeypress(p2_paddle.move_up, "Up")
screen.onkeypress(p2_paddle.move_down, "Down")


while game_started:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with upper and lower walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with Paddle
    if ball.distance(p2_paddle) < 40 and ball.xcor() > 350 or ball.distance(p1_paddle) < 40 and ball.xcor() < -350:
        ball.bounce_x()
        ball.increase_speed()

    # Detect right paddle misses
    if ball.xcor() < -380 or ball.xcor() > 380:
        if ball.xcor() < -380:
            score.p2_point()
        elif ball.xcor() > 380:
            score.p1_point()
        ball.reset_position()
        # ball.reset_speed()
screen.exitonclick()
