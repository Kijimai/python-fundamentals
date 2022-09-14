from turtle import Turtle, Screen
from state import StateManager
import time
import pandas as pd
# TODO:
# Add a Background using the image supplied
# import the states data from the csv file


screen = Screen()
screen.title("Name the States!")
screen.setup(width=725, height=491)
screen.bgpic('./blank_states_img.gif')
screen.tracer(0)
state_manager = StateManager()

data = pd.read_csv('./50_states.csv')
saved_states = pd.read_csv('./states_to_learn')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    time.sleep(0.1)
    answer_state = str(screen.textinput(
        title="Guess the State", prompt="What's another state's name? Type 'Q' to quit.")).title()
    if answer_state in guessed_states:
        pass
    elif answer_state in all_states:
        state_data = data[data["state"] == answer_state]
        state_coord = (int(state_data.x), int(state_data.y))
        state_manager.create_state(answer_state, state_coord)

    elif answer_state.lower() == "q":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    else:
        pass
# def get_mouse_click_coor(x, y):
#     print(x, y)


# screen.onscreenclick(get_mouse_click_coor)


# # For interactive use with the turtle screen
# screen.mainloop()
