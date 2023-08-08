from turtle import Screen, Turtle
import pandas as pd

# for the map
screen = Screen()
timmy = Turtle()
screen.title("U.S. States Game")
image = "day 21-30\\us state challenge\\blank_states_img.gif"
screen.addshape(image)
timmy.shape(image)

# for the state names 
tommy = Turtle()
tommy.hideturtle()
tommy.speed("fastest")
tommy.penup()

data = pd.read_csv("day 21-30\\us state challenge\\50_states.csv")
coordinates = list(zip(data["x"], data["y"]))
states = list(data["state"])

correct_guess = []
guess = 0
score = 0

while guess < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?", ).title()

    if answer_state == "Exit":
        break
    if answer_state in states:

        df_answer = data[data["state"] == answer_state][["x", "y"]]
        tuple_answer = list(zip(df_answer["x"], df_answer["y"]))[0]
        correct_guess.append(answer_state)
        states.remove(answer_state)

        tommy.goto(tuple_answer)
        tommy.write(answer_state)

        score += 1
    guess += 1
    print(guess)

new_data = pd.DataFrame(states)
new_data.to_csv("day 21-30\\us state challenge\\states_to_learn.csv")
