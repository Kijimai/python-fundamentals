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
game_started = True

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Extreme Ping Pong")
screen.listen()


ball = PongBall()
player_paddle = Paddle()
player_paddle.initial_position("player")
computer_paddle = Paddle()
computer_paddle.initial_position("computer")

screen.onkey(player_paddle.move_up, "Up")
screen.onkey(player_paddle.move_down, "Down")

screen.exitonclick()
