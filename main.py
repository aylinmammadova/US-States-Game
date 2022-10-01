import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")

# Setting turtle shape as image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting coordinates by mouse clicking
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# Loading our data
data = pandas.read_csv("50_states.csv")

guessed_states = []
score = 0
all_states = data["state"].to_list()
while len(guessed_states) < 50:

    # Asking user for an answer
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    # Exit the game and saving other states to a csv file
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df_states = pandas.DataFrame(missing_states)
        df_states.to_csv("States_to_learn.csv")
        break

    for state in data["state"]:
        if answer == state:

            # If state is already guessed don't execute code
            if state not in guessed_states:
                guessed_states.append(answer)

                # Getting coordinates of state
                state_data = data[data["state"] == answer]
                x_coor = state_data.x
                y_coor = state_data.y

                # Updating score
                score += 1

                # Write correct guess using coordinates on map
                new_state = turtle.Turtle()
                new_state.hideturtle()
                new_state.penup()
                new_state.setposition(int(x_coor), int(y_coor))
                new_state.write(state)
