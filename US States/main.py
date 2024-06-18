import turtle
from turtle import Screen
import pandas
image = "blank_states_img.gif"

screen = Screen()
screen.title("50 states of America")
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")

guessed_states = []
states = data["state"].to_list()

while len(guessed_states) < len(states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state's name?:  ").title()

    if answer_state in states:
        guessed_states.append(answer_state)
        p = turtle.Turtle()
        p.hideturtle()
        p.penup()
        x_cor = int(data[data["state"] == answer_state]['x'])
        y_cor = int(data[data["state"] == answer_state]['y'])
        p.goto(x_cor, y_cor)
        p.write(answer_state, align='center')
    elif answer_state == "Exit":
        # states_to_learn = []
        # for x in states:
        #     if x not in guessed_states:
        #         states_to_learn.append(x)
        states_to_learn = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("learn")
        break




