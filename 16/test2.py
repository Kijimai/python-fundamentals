# from turtle import Turtle, Screen
from turtle import *

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("", "lightgreen")

while True:
    my_turtle.forward(100)
    my_turtle.right(50)
    my_turtle.forward(25)
    my_turtle.stamp()
    if abs(my_turtle.pos()) < 1:
        break


my_screen = Screen()
my_screen.title = "My fancy turtle"
my_screen.exitonclick()
