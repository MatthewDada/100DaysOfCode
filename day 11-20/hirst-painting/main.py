import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
timmy.color("green")
timmy.speed("fastest")
turtle.colormode(255)


def draw_polygon(n):
    for i in range(n):
        timmy.forward(100)
        timmy.right(360/n)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size):
    for i in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(70)
        timmy.setheading(timmy.heading() + size)


draw_spirograph(5)
# draw_polygon(10)

screen = Screen()
screen.exitonclick()
