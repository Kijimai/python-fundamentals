from asyncore import read
from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ("arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('./score-data.txt') as data:
            self.high_score = int(data.read())
        self.pu()
        self.color("purple")
        self.goto(0, 200)
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./score-data.txt', mode="w") as file:
                file.write(f"{self.high_score}")
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   font=FONT_STYLE, align=ALIGNMENT)
