# Day 6 is a little different from the previous days

# Link to the game = https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Take your time to understand the game, try out the "Reeborg's keyboard" to understand how the game works.

# There is a drop down to play several levels of the game beside the "Reeborg's World".

# Code for the Hurdle 1
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while not wall_in_front():
        move()
    turn_left()
    
def up():
    turn_left()
    
    if wall_on_right():
        turn_left()
        while front_is_clear():
            move()
        turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        #move() 
"""



# My code for the maze 
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while not wall_in_front():
        move()
    turn_left()
    
def up():
    turn_left()
    
    if wall_on_right():
        turn_left()
        while front_is_clear():
            move()
        turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
"""