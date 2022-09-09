from turtle import Turtle


class Paddle(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.color("white")
        self.shape("square")

    def initial_position(self, type):
        if type == 'player':
            self.goto(-380, 0)

        elif type == "computer":
            self.goto(380, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y > 240:
            self.setposition(self.xcor(), 240)
        else:
            self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y < -230:
            self.setposition(self.xcor(), -230)
        else:
            self.setposition(self.xcor(), new_y)
