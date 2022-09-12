from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if FINISH_LINE_Y <= self.ycor():
            return True
        else:
            return False

    def reposition_start(self):
        self.goto(STARTING_POSITION)
