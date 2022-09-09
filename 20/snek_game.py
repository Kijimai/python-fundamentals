from turtle import Turtle, Screen
from random import randint
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# TODO:
# Create Snake Body x
# Move the Snake x
# Control the Snake x
# Detect Collision with food x
# Create a scoreboard x
# Detect collision with wall x
# Detect collision with tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnekGame")
screen.tracer(0)


score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(score.restart, "r")

game_started = True


def restart_game():
    score.restart()


while game_started:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_started = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_started = False
            score.game_over()

# Prevents automatic closing, can only close on user click
screen.exitonclick()
