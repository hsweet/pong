""" 
Minimal arcade program
Just enough to open a window with a color and draw a few simple shapes.
https://arcade-book.readthedocs.io/en/latest/chapters/06_drawing/drawing.html
"""
import arcade

arcade.open_window(300,300, "Pong")
arcade.set_background_color(arcade.color.BLUE)
#########
arcade.start_render()
# Draw stuff
arcade.draw_lrtb_rectangle_filled(25,35, 100,15, arcade.color.BITTER_LIME)
arcade.draw_rectangle_filled(250,100,10,90, arcade.color.LIME)
arcade.draw_point(50,50,arcade.color.GREEN,15)
#arcade.draw_circle()
#########
arcade.finish_render()
####  loop till user stops
arcade.run()
