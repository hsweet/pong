"""
Minimal arcade program
Just enough to open a window with a color and draw a few simple shapes.
https://arcade-book.readthedocs.io/en/latest/chapters/06_drawing/drawing.html
https://vimeo.com/168063840
"""
import arcade

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Rectangle Example"

# Size of the rectangle
WIDTH = 50
HEIGHT = 50

def on_draw(delta_time):
    ''' Changes the position of a Rectangle

    delta_time is how long since the last time the loop ran.
    If x is 2 then  x +=  is 3.  Its a shortcut for x = x + 1 '''

    arcade.start_render()
    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y, WIDTH, HEIGHT, arcade.color.GREEN)
    #
    on_draw.center_x += on_draw.delta_x * delta_time

    print(on_draw.center_x)

    #Back and forth in X direction
    if on_draw.center_x > SCREEN_WIDTH-WIDTH/2 or on_draw.center_x < WIDTH/2:
        on_draw.delta_x *= -1
    # add code here for Y direction    

on_draw.center_x = 100      # Initial x position
on_draw.center_y = 50       # Initial y position
on_draw.delta_x = 115  # Initial change in x
on_draw.delta_y = 130  # Initial change in y

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)

arcade.schedule(on_draw, 1 / 80)  # delta_time is decimal value of fraction

    # Run the program
arcade.run()
