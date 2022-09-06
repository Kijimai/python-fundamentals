from random import choice
from colorgram import colorgram
from turtle import Turtle, Screen
from color_list import rgb_colors
turtle = Turtle()
screen = Screen()
turtle.shape("arrow")
screen.colormode(255)
# colors = colorgram.extract("./hirst.jpg", 20)

turtle.setheading(220)
turtle.pu()
turtle.forward(300)
turtle.setheading(0)
turtle.speed(10)


for _ in range(10):
    turtle.pu()
    turtle.goto(-200, -200 + (_ * 50))
    turtle.pd()
    for _ in range(10):
        turtle.dot(20, choice(rgb_colors))
        turtle.pu()
        turtle.forward(50)
        turtle.pd()

screen.exitonclick()
