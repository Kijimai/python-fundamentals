from turtle import Screen
from state import StateManager
from score import ScoreBoard
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
scoreboard = ScoreBoard()
state_manager = StateManager()

data = pd.read_csv('./50_states.csv')
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
        state_coord = (float(state_data.x), float(state_data.y))
        state_manager.create_state(answer_state, state_coord)
        scoreboard.increase_score()
    elif answer_state.lower() == "q":
        break
    else:
        pass

# def get_mouse_click_coor(x, y):
#     print(x, y)


# screen.onscreenclick(get_mouse_click_coor)


# # For interactive use with the turtle screen
# screen.mainloop()
