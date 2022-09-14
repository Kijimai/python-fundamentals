from turtle import Turtle


class StateManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
    def create_state(self, name, coordinates):
        new_state = Turtle()
        new_state.pu()
        new_state.goto(coordinates)
        new_state.color("black")
        new_state.write(name)
