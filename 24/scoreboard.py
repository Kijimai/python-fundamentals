from turtle import Turtle, width
import pathlib

ALIGNMENT = "center"
FONT_STYLE = ("arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('./data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Current Score: {self.score} High Score: {self.high_score}",
                   font=FONT_STYLE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./data.txt', mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f"GAME OVER",
    #                font=FONT_STYLE, align=ALIGNMENT)

    # def restart(self):
    #     self.goto(0, 250)
    #     self.score = 0
    #     self.clear()
    #     self.write(f"Current Score: {self.score}",
    #                font=FONT_STYLE, align=ALIGNMENT)
