from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.forward(-10)


def move_left():
    current_pos = turtle.position()
    turtle.goto(current_pos[0] - 10, current_pos[1])


def move_right():
    current_pos = turtle.position()
    turtle.goto(current_pos[0] + 10, current_pos[1])


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def erase():
    turtle.reset()
    turtle.clear()


screen.listen()
screen.onkey(key='c', fun=turtle.clear())
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="q", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="e", fun=move_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=erase)
screen.exitonclick()
