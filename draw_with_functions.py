#! /usr/bin/python3.6
import arcade
import random

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 500

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing using Functions")
arcade.set_background_color(arcade.color.BLUE)
arcade.start_render()

def stickman(x,y):
    arcade.draw_rectangle_filled(x,y,10,100, arcade.color.DARK_CANDY_APPLE_RED)
    arcade.draw_point(x, y + 20, arcade.color.DARK_GOLDENROD,50)

def letter():
    pass

def draw_random(object):
    object (random.randint(10,400), random.randint (10,450))


# functions below draw different shapes.
# you call them using the function name, and the object to draw is
# inside the ()

def draw_horizontal(object):
    for x in range (1, 9):
        object (x * 50, 50)

def diagonal(object):
    for x in range (1, 500, 50):
        print(x)
        object (x , x )

def draw_x(object):
    # make an x
    for x in range (1,500, 50):
        y1 = x
        y2 = SCREEN_HEIGHT - y1
        object (x, y1)
        object (x, y2)

def grid(object):
    """ Draws a grid using nested loops.  This means the x loops
    """
    for x in range (1,9):
        for y in range (1, 9):
            object (x * 50, y * 50)

def pyramid(object, y, how_many):
    """ This function draws the object, changes the
    y value, reduces the number of x copies by one,
    then calls itself using the new numbers to draw the
    second row.  It repeats this till there is only one object
    at the top of the screen.  This is known as a recursive function
    """
    for x in range(how_many):
        object(x * 50 , y)
    y += 50                 # draw next row higher
    how_many -= 1           # make one fewer copy
    if how_many > 0:        # stop at one
        pyramid(object, y, how_many)

# move call to draw_x function to menu
for location in range (10):
    draw_random (stickman)

'''
#    Menu
pattern  = input ('Choose Pattern, h/d/g/p ')

if pattern == 'h':
    draw_horizontal(stickman)
elif pattern == 'd':
    draw_diagonal(stickman)
elif pattern == 'g':
    draw_grid(stickman)
elif pattern == 'p':
    draw_pyramid(stickman, 25, 10)
'''

arcade.finish_render()
arcade.run()
