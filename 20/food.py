from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # Initialize a randomly placed food object between -280 x/y coordinates
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))
      