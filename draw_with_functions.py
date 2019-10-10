#! /usr/bin/python3.6
import arcade

""" assignment:

 1. Make a new SIMPLE !!!!!  object, similar to stickman
 2. Change the code to call your object instead of stickman()
 3. Make a function called vertical() that draws a stack of your object
 4. Draw an X.  Hint.  modify the diagonal() function with negative numbers
 5. Use print() to see how the x and y values change in the grid looop.
 6. Add your functions to the input () statement so they can be chosen in the menu

"""

arcade.open_window(450,550, "Drawing using Functions")
arcade.set_background_color(arcade.color.BLUE)
arcade.start_render()

def stickman(x,y):
    arcade.draw_rectangle_filled(x,y,10,100, arcade.color.DARK_CANDY_APPLE_RED)
    arcade.draw_point(x, y + 20, arcade.color.DARK_GOLDENROD,50)

def horizontal(object):
    for x in range (1, 9):
        object (x * 50, 50)

def diagonal(object):
    for x in range (1, 500, 50):
        print(x)
        object (x , x )

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
    y += 50                 # higher next row
    how_many -= 1           # one fewer copy
    if how_many > 0:        # stop at one
        pyramid(object, y, how_many)

pattern  = input ('Choose Pattern, h/d/g/p ')

if pattern == 'h':
    horizontal(stickman)
elif pattern == 'd':
    diagonal(stickman)
elif pattern == 'g':
    grid(stickman)
elif pattern == 'p':
    pyramid(stickman, 25, 10)

arcade.finish_render()
arcade.run()
