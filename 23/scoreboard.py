from turtle import Turtle, color

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
