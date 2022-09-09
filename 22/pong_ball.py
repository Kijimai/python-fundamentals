from turtle import Turtle


class PongBall(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()

    def move(self):
        self.forward(10)
