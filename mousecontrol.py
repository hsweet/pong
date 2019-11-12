import arcade

# Based on Paul Craven's Arcade Academy code

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
  def __init__(self, position_x, position_y, radius, color):

      # Take the parameters of the init function above, and create instance variables out of them.
      self.position_x = position_x
      self.position_y = position_y
      self.radius = radius
      self.color = color

  def draw(self):
      """ Draw the balls with the instance variables we have. """
      arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

class MyGame(arcade.Window):

  def __init__(self, width, height, title):

      # Call the parent class's init function
      super().__init__(width, height, title)

      # Make the mouse disappear when it is over the window.
      # So we just see our object, not the pointer.
      #self.set_mouse_visible(False)

      arcade.set_background_color(arcade.color.ASH_GREY)

      # Create our ball
      self.ball = Ball(320, 240, 15, arcade.color.AUBURN)

  def on_draw(self):
      """ Called whenever we need to draw the window. """
      arcade.start_render()
      self.ball.draw()

  def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second.

        Move the ball up and down faster or slower depending  on how far
        the mouse has moved
        x and y = the current location of the mouse pointer,
        dx and dy = the distance the mouse has moved since the last check
        """
        print (dx, dy)
        if dy > 0:
            for m in range (5):
                self.ball.position_y += dy / 2
                if self.ball.position_y > SCREEN_HEIGHT:
                    self.ball.position_y = 20
        elif dy < 0:
            for m in range (5):
                self.ball.position_y -= dy / -2
                if self.ball.position_y < 0:
                    self.ball.position_y = SCREEN_HEIGHT

  def on_mouse_press(self, x, y, button, modifiers):
    """ Called when the user presses a mouse button. """

    if button == arcade.MOUSE_BUTTON_LEFT:
        print("Left mouse button pressed at", x, y)
        self.ball.radius *=2
    elif button == arcade.MOUSE_BUTTON_RIGHT:
        print("Right mouse button pressed at", x, y)
        self.ball.radius /= 2

def main():
  window = MyGame(640, 480, "Indirect Mouse Control")
  arcade.run()

main()
