#! /usr/bin/python3.6
import arcade

arcade.open_window(300,300, "Drawing using Functions")
arcade.set_background_color(arcade.color.BLUE)
arcade.start_render()

def stickman(x,y):
    arcade.draw_rectangle_filled(x,y,10,100, arcade.color.DARK_CANDY_APPLE_RED)
    arcade.draw_point(x, y + 20, arcade.color.DARK_GOLDENROD,50)

for x in range (10):
    for y in range (10):
        stickman(x * 40, y * 40)

arcade.finish_render()
arcade.run()
