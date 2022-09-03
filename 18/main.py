from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.bgcolor("orange")
turtle.shape("turtle")
turtle.color("green", "lightgreen")
turtle.speed(10)


def draw_shape(shape):
    if shape.lower() == "triangle":
        for _ in range(3):
            turtle.forward(100)
            turtle.right(120)
    elif shape.lower() == "square":
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif shape.lower() == "pentagon":
        for _ in range(5):
            turtle.forward(100)
            turtle.right(72)
    elif shape.lower() == "hexagon":
        for _ in range(6):
            turtle.forward(100)
            turtle.right(60)
    elif shape.lower() == "heptagon":
        for _ in range(7):
            turtle.forward(100)
            turtle.right(360 / 7)
    elif shape.lower() == "octagon":
        for _ in range(8):
            turtle.forward(100)
            turtle.right(45)
    elif shape.lower() == "nonagon":
        for _ in range(9):
            turtle.forward(100)
            turtle.right(40)
    elif shape.lower() == "decagon":
        for _ in range(10):
            turtle.forward(100)
            turtle.right(36)


draw_shape("triangle")
draw_shape("square")
draw_shape("pentagon")
draw_shape("hexagon")
draw_shape("heptagon")
draw_shape("octagon")
draw_shape("nonagon")
draw_shape("decagon")

screen.exitonclick()


# Draw a square
# while True:
#     turtle.forward(100)
#     turtle.right(90)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.pu()
# turtle.goto(-400, 0)

# for _ in range(50):
#   turtle.pd()
#   turtle.forward(8)
#   turtle.pu()
#   turtle.forward(8)
