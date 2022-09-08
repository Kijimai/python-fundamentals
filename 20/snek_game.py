from turtle import Turtle, Screen
from random import randint
from snake import Snake
from food import Food
import time

# TODO:
# Create Snake Body
# Move the Snake
# Control the Snake
# Detect Collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnekGame")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_started = True

while game_started:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()


# Prevents automatic closing, can only close on user click
screen.exitonclick()
