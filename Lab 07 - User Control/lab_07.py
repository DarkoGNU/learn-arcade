""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


def draw_ground():
    """ Draws some grass """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.LIGHT_GREEN)


def draw_tree(x, y):
    """ Draws a tree with acorns """
    # Draw a trunk
    arcade.draw_rectangle_filled(x, y - 15, 20, 50, arcade.csscolor.SIENNA)

    # Draw the leaves
    arcade.draw_triangle_filled(x1=x - 30, y1=y + 10, x2=x + 30, y2=y + 10, x3=x, y3=y + 60, color=arcade.csscolor.GREEN)

    # Draw some "acorns"
    arcade.draw_point(x + 5, y + 18, arcade.csscolor.BROWN, 5)
    arcade.draw_point(x + 12, y + 16, arcade.csscolor.BROWN, 5)
    arcade.draw_point(x - 16, y + 31, arcade.csscolor.BROWN, 5)
    arcade.draw_point(x - 5, y + 41, arcade.csscolor.BROWN, 5)
    arcade.draw_point(x + 6, y + 41, arcade.csscolor.BROWN, 5)

    # Check center
    arcade.draw_point(x, y, arcade.csscolor.RED, 5)


class StickMan:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        """ Draw the StickMan with the instance variables we have. """
        draw_stick_man(self.position_x, self.position_y)


def draw_stick_man(x, y):
    # Legs
    arcade.draw_line(x - 15, y - 30, x, y - 10, arcade.csscolor.BLACK, 5)
    arcade.draw_line(x + 15, y - 30, x, y - 10, arcade.csscolor.BLACK, 5)

    # "Gut"
    arcade.draw_line(x, y - 10, x, y + 10, arcade.csscolor.BLACK, 5)

    # Arms
    arcade.draw_line(x, y + 10, x - 15, y - 10, arcade.csscolor.BLACK, 5)
    arcade.draw_line(x, y + 10, x + 15, y - 10, arcade.csscolor.BLACK, 5)

    # Head
    arcade.draw_circle_outline(x, y + 20, 10, arcade.csscolor.BLACK, 5)

    # Check center
    arcade.draw_point(x, y, arcade.csscolor.RED, 5)


class Sun:
    def __init__(self, position_x, position_y, bump_sound):
        self.position_x = position_x
        self.position_y = position_y
        self.bump_sound = bump_sound
        self.bump_player = None

    def draw(self):
        draw_sun(self.position_x, self.position_y)

    def play_sound(self):
        if not self.bump_player or not self.bump_player.playing:
            self.bump_player = self.bump_sound.play()

    def update(self, keys):
        if keys["W"] and not keys["S"]:
            self.position_y += MOVEMENT_SPEED
        elif keys["S"] and not keys["W"]:
            self.position_y -= MOVEMENT_SPEED

        if keys["D"] and not keys["A"]:
            self.position_x += MOVEMENT_SPEED
        elif keys["A"] and not keys["D"]:
            self.position_x -= MOVEMENT_SPEED

        # Prevent the Sun from going off-screen

        if self.position_x + 50 > SCREEN_WIDTH:
            self.position_x = SCREEN_WIDTH - 50
            self.play_sound()
        elif self.position_x - 50 < 0:
            self.position_x = 50
            self.play_sound()

        if self.position_y + 50 > SCREEN_HEIGHT:
            self.position_y = SCREEN_HEIGHT - 50
            self.play_sound()
        elif self.position_y - 50 < 0:
            self.position_y = 50
            self.play_sound()


def draw_sun(x, y):
    arcade.draw_circle_filled(x, y, 30, arcade.csscolor.YELLOW)

    # Draw straight rays
    arcade.draw_line(x, y - 50, x, y + 50, arcade.csscolor.YELLOW, 5)
    arcade.draw_line(x - 50, y, x + 50, y, arcade.csscolor.YELLOW, 5)

    # Draw diagonal rays
    arcade.draw_line(x - 40, y - 40, x + 40, y + 40, arcade.csscolor.YELLOW, 5)
    arcade.draw_line(x + 40, y - 40, x - 40, y + 40, arcade.csscolor.YELLOW, 5)

    # Check center
    arcade.draw_point(x, y, arcade.csscolor.RED, 5)


class MyGame(arcade.Window):
    """ Our Custom Window Class """

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Background color
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Hide the mouse
        self.set_mouse_visible(False)

        # Make a man
        self.man = StickMan(50, 50)

        # Make the Sun
        self.sun = Sun(100, 500, arcade.load_sound(":resources:sounds/lose1.wav"))

        # Keys pressed dictionary
        self.keys = {"A": False, "D": False, "W": False, "S": False}

        # Sounds
        self.mouse_sound = arcade.load_sound(":resources:sounds/error4.wav")

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        # Draw ground
        draw_ground()

        # Draw some trees
        draw_tree(50, 50)
        draw_tree(562, 74)
        draw_tree(124, 126)
        draw_tree(264, 20)
        draw_tree(468, 186)
        draw_tree(500, 65)

        # Draw some people
        draw_stick_man(400, 70)
        draw_stick_man(300, 140)
        draw_stick_man(150, 30)
        draw_stick_man(450, 170)

        # Draw the sun
        self.sun.draw()

        # Draw the ball
        self.man.draw()

        # Finish the render
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second. """
        self.man.position_x = x
        self.man.position_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.keys["W"] = True
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.keys["S"] = True
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.keys["A"] = True
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.keys["D"] = True

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.mouse_sound.play()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.keys["W"] = False
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.keys["S"] = False
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.keys["A"] = False
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.keys["D"] = False

    def on_update(self, delta_time: float):
        # Update the Sun
        self.sun.update(self.keys)


def main():
    window = MyGame()
    arcade.run()


main()
