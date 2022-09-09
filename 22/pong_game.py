# Create The screen
# Create and Move the paddle
# Create another paddle (Computer)
# Detect Collision with wall and bounce
# Detect Collision with paddle
# Create score for each player
# Detect when paddle misses and hits behind opposite player's paddle
from pong_ball import PongBall
from turtle import Turtle, Screen

game_started = True

# Screen Setup
screen = Screen()
screen.setup(width=600, height=800)
screen.colormode(255)
screen.bgcolor("black")

ball = PongBall()

screen.exitonclick()
