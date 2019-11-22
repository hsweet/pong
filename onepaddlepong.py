#!/usr/bin/python3
''' Simple Pong game, code built on arcade template from
https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade
'''
import arcade
from arcade.geometry import check_for_collision
import random

WIDTH = 600
HEIGHT = 400
TITLE = 'One Paddle Pong'

class IntroView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Click to begin", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = Pong()
        self.window.show_view(game)

class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        exit()


#class Pong(arcade.Window):
class Pong(arcade.View):


    """ Main application class. """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ball_sound = arcade.load_sound("resources/coin1.wav")
        self.paddle_sound = arcade.load_sound("resources/jump1.wav")
        self.lose_sound = arcade.load_sound("resources/laser1.wav")
        self.background_sound = arcade.load_sound("resources/serba.wav")

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)
        #self.set_mouse_visible(False)
        self.player_paddle = arcade.Sprite('resources/paddle.png',1)
        self.ball = arcade.Sprite('resources/ball.png')

        self.start_ball()

    def start_ball(self):
        # direction also affects speed
        self.direction_x = 1
        self.direction_y = 1
        self.speed = 7
        self.player_paddle.center_x = WIDTH - 10
        self.player_paddle.center_y = 50
        self.ball.center_x = 10
        self.ball.center_y = random.randint (10, HEIGHT - 10)
        #self.ball.center_y = 10
        print (f"starting ball at {self.ball.center_x},{self.ball.center_y}")
        arcade.play_sound(self.background_sound)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_paddle.draw()
        self.ball.draw()
        arcade.draw_text('Score: ' + str(self.score) , 50, 50, arcade.color.BLACK, 16)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here.
         """
        # print (delta_time)
        self.ball.center_x += self.direction_x * self.speed   # move to the right
        self.ball.center_y += self.direction_y * self.speed  # move up and down
        #print (int(self.ball.center_x) , end = " ")
        # next make ball start from random spot move in random direction
        # bounce off walls and paddle.
        if check_for_collision (self.ball, self.player_paddle) == True:
           self.score += 10
           arcade.play_sound(self.paddle_sound)
           # keeps ball from bouncing back and forth when it hits paddle end
           #self.ball.center_x = WIDTH - WIDTH / 10
           self.direction_x *= -1
        elif self.ball.center_x > WIDTH :
            # player misses ball
            arcade.play_sound(self.lose_sound)
            arcade.pause(2)
            self.score -= 1
            self.start_ball()
        elif self.ball.center_x <10:
            self.direction_x *= -1
            arcade.play_sound(self.ball_sound)
        elif self.ball.center_y > HEIGHT or self.ball.center_y < 10:
            self.direction_y *= -1
            arcade.play_sound(self.ball_sound)
        elif self.score > 30:
            print ('Winner')
            arcade.draw_text('You Win! ', 100, 100, arcade.color.RED, 36)
            arcade.start_render()
            arcade.pause(5)
            exit()

    def on_key_press(self, key, key_modifiers):
        # this needs code to keep paddle on screen
        if key == arcade.key.UP:
            self.player_paddle.center_y += 30
        elif key == arcade.key.DOWN:
            self.player_paddle.center_y += -30
        elif key == arcade.key.Q:
            #arcade.stop_sound(self.background_sound)
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)


    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        def on_mouse_press(self, _x, _y, _button, _modifiers):
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)


def main():

    '''a main() function is not necessary unless you use this as a module
     you import into another program. The code in main() will only runs if
      it is not imported.  If it is imported you can use all the methods.
    '''
    window = arcade.Window(WIDTH, HEIGHT, "One Paddle Pong")
    intro_view = IntroView()
    window.show_view (intro_view)
    #game = Pong(WIDTH, HEIGHT, TITLE)
    #game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
