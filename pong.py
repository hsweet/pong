"""
Minimal arcade program
Just enough to open a window with a color and draw a few simple shapes.
https://arcade-book.readthedocs.io/en/latest/chapters/06_drawing/drawing.html
"""
import arcade, random

# Size of the screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Trevors Pong"

# Size of the rectangle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 90

arcade.open_window(300,300, "Pong")
arcade.set_background_color(arcade.color.BLUE)

#########
def draw():
	arcade.start_render()
	# Draw stuff
	arcade.draw_rectangle_filled(25,35, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.LIME)
	arcade.draw_rectangle_filled(250,100, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.LIME)
	arcade.draw_point(50,50,arcade.color.GREEN,15)
	x=arcade.load_texture('paddle.png')
	arcade.draw_texture_rectangle, 50,50,100,100,2)

#########
draw()
arcade.finish_render()
####  loop till user stops
arcade.run()
