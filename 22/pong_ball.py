from turtle import Turtle


class PongBall(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.speed = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self):
        self.speed += 0.01
        self.x_move *= self.speed
        self.y_move *= self.speed

    def reset_speed(self):
        self.speed = 1
        self.x_move *= self.speed
        self.y_move *= self.speed
