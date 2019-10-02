#https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade

import arcade
from arcade.geometry import check_for_collision
   
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE='One Paddle Pong'

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height,title):
        super().__init__(width, height,title)
        arcade.set_background_color(arcade.color.AMAZON)
        #self.paddles = None
        #self.ball = None
        self.score = 0
        # self.set_mouse_visible(False)

    def setup(self):
        # Set up your game here
        self.player_paddle = arcade.Sprite('paddle.png',1)
        self.ball = arcade.Sprite('ball.png')
        
        self.player_paddle.center_x = SCREEN_WIDTH -50
        self.player_paddle.center_y = 50
        
        self.ball.center_x = 10
        self.ball.center_y = SCREEN_HEIGHT /2

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_paddle.draw()
        self.ball.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here.
        also called animate method """
        self.ball.center_x += 3  #move to the right
        if check_for_collision (self.ball, self.player_paddle) == True:
           print ('hit')
           self.ball.center_x = 0
          
       # x=arcade.check_for_collision_with_list(self.player_paddle, self.ball)
         
    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player_paddle.center_y += 30
        elif key == arcade.key.DOWN:
            self.player_paddle.center_y += -30
        
    def on_key_release(self, key, key_modifiers):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
