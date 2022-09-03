from turtle import Turtle, Screen
from random import choice, randint

directions = [0, 90, 180, 270]

screen = Screen()
turtle = Turtle()
screen.colormode(255)

turtle.shape("arrow")
turtle.speed(10)
turtle.pensize(15)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for _ in range(100):
    turtle.forward(50)
    turtle.color(random_color())
    print(random_color())
    turtle.setheading(choice(directions))

screen.exitonclick()
