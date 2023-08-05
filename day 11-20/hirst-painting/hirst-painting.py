import turtle
from turtle import Turtle, Screen
import random

"""
# Downloaded a hirst painting picture with the name 'image.jpeg'
color_list = cg.extract("image.jpeg", 30)
color = []

for i in range(len(color_list)):
    rgb = color_list[i]
    r = rgb.rgb.r
    g = rgb.rgb.g
    b = rgb.rgb.b
    new_color = (r, g, b)
    color.append(new_color)"""

# The color_list below is the result of the lines of code above.


# My own solution below.
color_list = [(246, 240, 228), (248, 237, 243), (234, 246, 239), (235, 240, 247), (196, 153, 117), (139, 71, 89),
              (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15),
              (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19),
              (83, 156, 112), (223, 172, 184), (227, 175, 167), (103, 44, 60), (50, 56, 94), (168, 207, 185),
              (167, 158, 66), (60, 155, 174), (111, 122, 155), (97, 49, 44), (178, 188, 214)]

timmy = Turtle()
timmy.speed("fastest")
turtle.colormode(255)
timmy.hideturtle()


def draw_horizontal(size, space, horizontal_count):
    for i in range(horizontal_count + 1):
        timmy.dot(size, random.choice(color_list))
        timmy.penup()
        timmy.setx(i * (size + space))
        timmy.pendown()


def painting(vertical_count):
    i = 0
    y_position = 0
    while i < vertical_count:
        draw_horizontal(size=15, space=20, horizontal_count=10)
        timmy.penup()
        timmy.setx(0)
        y_move = y_position + 30
        timmy.sety(y_move)
        y_position += 30
        timmy.pendown()
        i += 1


painting(10)


# Course solution
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# tim.colormode(255)

color_list_ = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
               (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
               (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
               (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17,20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
               (174, 94, 97), (176, 192, 209)]

# go to a new position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list_))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
