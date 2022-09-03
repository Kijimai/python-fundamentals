from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.shape("circle")
turtle.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_spirograph(gapsize):
    for _ in range(int(360 / gapsize)):
        turtle.color(random_color())
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + gapsize)


draw_spirograph(5)

screen.exitonclick()
