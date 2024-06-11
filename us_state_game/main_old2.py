import turtle as t
import pandas as pd

#Setting screen
screen = t.Screen()
us_map = t.Turtle()
screen.title("U.S. States Game")
US_STATES_IMAGE = "./blank_states_img.gif"

screen.addshape(US_STATES_IMAGE)
us_map.shape(US_STATES_IMAGE)


#States names document
csv_data = pd.read_csv("50_states.csv")
states_list = csv_data.state.to_list()

corrected_states = []

while len(corrected_states) < len(states_list):
    # Asking states
    user_input = screen.textinput(f"{len(corrected_states)} / {len(states_list)} States",
                                  "What's another states name? ").title()

    if user_input == "Exit":
        left_states = []

        for state in states_list:
            if state not in corrected_states:
                left_states.append(state)

        will_study_states = pd.DataFrame(left_states)
        will_study_states.to_csv("states_to_learn.csv")
        break

    #Checking states in States
    if user_input in states_list:
        corrected_states.append(user_input)
        display = t.Turtle()
        display.penup()
        display.hideturtle()
        state_data = csv_data[csv_data.state == user_input]
        display.goto(int(state_data.x), int(state_data.y))
        display.color("red")
        display.write(state_data.state.item())


