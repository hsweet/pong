import arcade, random
"""
Practice basic arcade drawing commands and some practice using the
arcade api (application programing interface)
This is a list of all the various arcade functions, methods, classes
and all the detail you need to program with arcade and Python
 http://arcade.academy/index.html
 http://arcade.academy/quick_index.html def on_mouse_press(self, x, y, button, modifiers):
        vertical(10,random.randint(10),x,y)
 http://arcade.academy/arcade.color.html
"""
######## setup stuff ##########################

screen_width = 1280
screen_height = 960
def drawA(xPos,yPos):
        arcade.draw_line(0+xPos,0+yPos,15+xPos,30+yPos,arcade.color.BLUE,5)
        arcade.draw_line(15+xPos,30+yPos,30+xPos,0+yPos,arcade.color.BLUE,5)
        arcade.draw_line(5+xPos,15+yPos,25+xPos,15+yPos,arcade.color.BLUE,5)
def vertical(amount,times,xPos,yPos):
        goDown = 0
        for i in range(0,times):
                drawA(xPos,yPos-goDown)
                goDown += amount
                
#################################################
        
class Drawd(arcade.Window):


        def setup(self):
                arcade.set_background_color(arcade.color.AMAZON)
        def on_draw(self):
                arcade.start_render()
        def on_mouse_press(self, x, y, button, modifiers):
                print("x=", x, "y=", y, "button=", button)
                vertical(10,random.randint(2,10),x,y)

game = Drawd(screen_width, screen_height, "Agd;lka")
game.setup()
arcade.run()   # game loop
