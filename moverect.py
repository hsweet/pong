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

 
#arcade.open_window(300,300, "Pong")
#arcade.set_background_color(arcade.color.BLUE)
#########
#arcade.start_render()
# Draw stuff
#arcade.draw_lrtb_rectangle_filled(25,35, 100,15, arcade.color.BITTER_LIME)
#arcade.draw_rectangle_filled(250,100,10,90, arcade.color.LIME)
#arcade.draw_point(50,50,arcade.color.GREEN,15)
#########

def on_draw(delta_time):
	arcade.start_render()
	arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y, WIDTH, HEIGHT, arcade.color.GREEN)
	#  += assigns result of addition to first operand, so below it increments on_draw.center_x
	on_draw.center_x += on_draw.delta_x * delta_time
	 
	print(on_draw.center_x)
	 
	
	#Back and forth in X direction
	if on_draw.center_x > SCREEN_WIDTH-WIDTH/2 or on_draw.center_x < WIDTH/2:
		on_draw.delta_x *= -1
		on_draw.center_y += 10
	 

 
on_draw.center_x = 100      # Initial x position
on_draw.center_y = 50       # Initial y position
on_draw.delta_x = 115  # Initial change in x
on_draw.delta_y = 130  # Initial change in y

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)
#arcade.finish_render()

arcade.schedule(on_draw, 1 / 80)  # delta_time is decimal value of fraction 

    # Run the program
arcade.run()
