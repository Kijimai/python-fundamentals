from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake:
    """Creates a 3 segment snake"""
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.pu()
            turtle.goto(position)
            self.segments.append(turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
      if self.head.heading() != DOWN:
        self.head.setheading(UP)

    def down(self):
      if self.head.heading() != UP:
        self.head.setheading(DOWN)

    def left(self):
      if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)

    def right(self):
      if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)