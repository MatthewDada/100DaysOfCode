from turtle import Turtle, Screen
import random

screen = Screen()
race_on = True

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "Slateblue3"]
names = ["tammy", "temmy", "timmy", "tommy", "tummy", "tim", "tom"]
y = -100

for i in range(0, len(colors)):
    names[i] = Turtle(shape="turtle")
    names[i].penup()
    names[i].color(colors[i])
    names[i].goto(x=-235, y=y)
    y += 40

if user_bet:
    race_on = True

while race_on:

    for turtle in names:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won.")
            else:
                print(f"You lost! The {winning_color} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
