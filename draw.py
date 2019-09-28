import arcade, random
"""
Practice basic arcade drawing commands and some practice using the 
arcade api (application programing interface)
This is a list of all the various arcade functions, methods, classes
and all the detail you need to program with arcade and Python
 http://arcade.academy/index.html
 http://arcade.academy/quick_index.html
 http://arcade.academy/arcade.color.html
"""
######## setup stuff ##########################
screen_width = 600
screen_height = 300
arcade.open_window(screen_width,screen_height,"Lines")
arcade.set_background_color(arcade.color.BLUE)
#################################################
arcade.start_render()

for point in range(100):
	point=( (random.randint(0,screen_width),random.randint(0,screen_height)))
	arcade.draw_point(point[0],point[1], arcade.color.GREEN, 9)	

arcade.draw_line(0,0,30,30,arcade.color.BLACK,5)

lines=((20,30),(60,90),(40,50),(90,120))
arcade.draw_lines(lines,arcade.color.BLACK, 1)

for point in range(1000):
	point=( (random.randint(0,screen_width),random.randint(0,screen_height)))
	arcade.draw_line(point[0],point[1],100,100, arcade.color.RED, 1)

arcade.finish_render()
arcade.run()   # game loop
