from turtle import Turtle, Screen
import pandas as pd

tr = Turtle()

screen = Screen()
screen.setup(height=500, width=720)
screen.bgpic("blank_states_img.gif")

tr.hideturtle()
tr.penup()
tr.speed("fastest")

states = {}

data = pd.read_csv("50_states.csv")
for i in range(len(data)):
    state = data.iloc[i]["state"].lower()
    x = data.iloc[i]["x"]
    y = data.iloc[i]["y"]

    states[state] = (x, y)

user_guessed = []

is_game_on = True
while len(user_guessed) < len(data) and is_game_on:
    user_guess = screen.textinput(title=f"{len(user_guessed)} / {len(data)} State Correct", prompt="Enter any State name: ").lower()
    if user_guess == "exit":
        is_game_on = False
        screen.bye()
    if states.get(user_guess):
        if user_guess not in user_guessed:
            tr.goto(states.get(user_guess))
            tr.write(user_guess.title(), align="center", font=("Courier", 8, "bold"))
            user_guessed.append(user_guess)

