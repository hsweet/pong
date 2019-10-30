import arcade, random
 
######## setup stuff ##########################

SCREEN_WIDTH = 200  #constants should be in CAPS
SCREEN_HEIGHT = 200

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Letter")
arcade.set_background_color(arcade.color.AMAZON)
arcade.start_render()

################### end setup #####################

def drawA(xPos,yPos):
    arcade.draw_line(0 + xPos,0 + yPos,15 + xPos,30 + yPos, arcade.color.BLUE,5)
    arcade.draw_line(15+xPos,30+yPos,30+xPos,0+yPos,arcade.color.BLUE,5)
    arcade.draw_line(5+xPos,15+yPos,25+xPos,15+yPos,arcade.color.BLUE,5)

def vertical(amount,times,xPos,yPos):
    goDown = 0
    for i in range(0,times):
        drawA(xPos,yPos-goDown)
        goDown += amount

vertical(20, 10, 10, 100)

arcade.finish_render()
arcade.run()   # game loop
