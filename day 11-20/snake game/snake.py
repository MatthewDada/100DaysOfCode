from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[num - 1].xcor()
            new_y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(new_x, new_y)

        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
