from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ("arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.color('white')
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.goto(-100, 200)
        self.write(self.p1_score, align=ALIGNMENT, font=FONT_STYLE)
        self.goto(100, 200)
        self.write(self.p2_score, align=ALIGNMENT, font=FONT_STYLE)

    def p1_point(self):
        self.p1_score += 1
        self.update_score()

    def p2_point(self):
        self.p2_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align=ALIGNMENT, font=FONT_STYLE)
        self.goto(100, 200)
        self.write(self.p2_score, align=ALIGNMENT, font=FONT_STYLE)
