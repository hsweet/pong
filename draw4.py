import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Letter(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height,title):
        super().__init__(width, height,title)

        arcade.set_background_color(arcade.color.AMAZON)

    def drawA(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        print (self.xPos, self.yPos)
        arcade.draw_line(0 + self.xPos,0 + self.yPos,15 + self.xPos,30 + self.yPos, arcade.color.BLUE,5)
        arcade.draw_line(15 + xPos, 30 + yPos, 30 + xPos, 0 + yPos, arcade.color.BLUE,5)
        arcade.draw_line(5 + xPos, 15 + yPos, 25 + xPos, 15 + yPos, arcade.color.BLUE,5)

    def vertical(self, amount, times, xPos, yPos):
        self.amount = amount
        self.times = times
        self.xPos = xPos
        self.yPos = yPos
        self.goDown = 0
        for i in range(0, times):
            self.drawA(self.xPos, self.yPos - self.goDown)
            self.goDown += self.amount

def main():
  # make an instance of Letter class
   let = Letter(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Letter')
   # start_render() BEFORE drawing
   arcade.start_render()
   let.drawA(300,100)
   let.vertical(30, 10, 100, 500)
   arcade.run()


if __name__ == "__main__":
   main()
