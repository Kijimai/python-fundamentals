# Ask the user for their bet "Who will win the race?"
# store the input into a variable
# Instantiate 6 turtle objects
# Each turtle should have their own color
# [red, green, blue, purple, yellow, orange]
# each turtle will be repositioned to the left side of the screen at different heights, each spaced out at least 20px
# Each turtle will move forward a random integer amount

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = True

colors = ['red', 'orange', 'purple', 'green', 'yellow', 'blue']
all_turtles = []
prediction = screen.textinput(
    title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.pu()
    turtle.goto(x=-230, y=30 * turtle_index)
    turtle.color(colors[turtle_index])
    all_turtles.append(turtle)

while is_race_on:
  for turtle in all_turtles:
    random_distance = randint(0, 10)
    turtle.forward(random_distance)

screen.exitonclick()
