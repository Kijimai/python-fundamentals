import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
car_director = CarManager()
score = Scoreboard()
screen.onkeypress(turtle.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_director.create_car()
    car_director.move_cars()

    for car in car_director.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

    if turtle.is_at_finish_line():
        turtle.reposition_start()
        car_director.level_up()
        score.increase_level()


screen.exitonclick()
