from turtle import Turtle, width

ALIGNMENT = "center"
FONT_STYLE = ("arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Current Score: {self.score}",
                   font=FONT_STYLE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER",
                   font=FONT_STYLE, align=ALIGNMENT)

    def update(self):
        self.clear()
        self.color("white")
        self.write(f"Current Score: {self.score}",
                   font=FONT_STYLE, align=ALIGNMENT)

    # def restart(self):
    #     self.goto(0, 250)
    #     self.score = 0
    #     self.clear()
    #     self.write(f"Current Score: {self.score}",
    #                font=FONT_STYLE, align=ALIGNMENT)
