"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""
import copy

from config import *

import random
import arcade
from pyglet.math import Vec2


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Wall grid - for coin placement
        self.wall_grid = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world', but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def make_wall(self, center_x, center_y):
        texture = WALL_TEXTURES[random.randrange(4)]

        self.wall_list.append(arcade.Sprite(
                filename=texture, scale=SPRITE_SCALING,
                center_x=center_x, center_y=center_y))

    def create_walls(self):
        for row in range(MAZE_HEIGHT):
            # Actual walls
            self.make_wall(0, row * WALL_HEIGHT)
            self.make_wall(MAZE_WIDTH * WALL_WIDTH, row * WALL_HEIGHT)

            # The grid
            self.wall_grid[row][0] = True
            self.wall_grid[row][MAZE_WIDTH] = True

        for column in range(MAZE_WIDTH + 1):
            # Actual walls
            self.make_wall(column * WALL_WIDTH, 0)
            self.make_wall(column * WALL_WIDTH, MAZE_HEIGHT * WALL_HEIGHT)

            # The grid
            self.wall_grid[0][column] = True
            self.wall_grid[MAZE_HEIGHT][column] = True

    def create_maze(self, top, bottom, left, right):
        """
        Recursive function to divide up the maze in four sections
        and create three gaps.
        Walls can only go on even numbered rows/columns.
        Gaps can only go on odd numbered rows/columns.
        Maze must have an ODD number of rows and columns.
        """

        # Figure out where to divide horizontally
        start_range = bottom + 2
        end_range = top - 1
        y = random.randrange(start_range, end_range, 2)

        # Do the division
        for column in range(left + 1, right):
            self.make_wall(column * WALL_WIDTH, y * WALL_HEIGHT)
            self.wall_grid[y][column] = True

        # Figure out where to divide vertically
        start_range = left + 2
        end_range = right - 1
        x = random.randrange(start_range, end_range, 2)

        # Do the division
        for row in range(bottom + 1, top):
            self.make_wall(x * WALL_WIDTH, row * WALL_WIDTH)
            self.wall_grid[row][x] = True

        # Now we'll make a gap on 3 of the 4 walls.
        # Figure out which wall does NOT get a gap.
        wall = random.randrange(4)
        if wall != 0:
            gap = random.randrange(left + 1, x, 2)
            arcade.get_sprites_at_point((gap * WALL_WIDTH, y * WALL_HEIGHT), self.wall_list)[0].remove_from_sprite_lists()
            self.wall_grid[y][gap] = False

        if wall != 1:
            gap = random.randrange(x + 1, right, 2)
            arcade.get_sprites_at_point((gap * WALL_WIDTH, y * WALL_HEIGHT), self.wall_list)[0].remove_from_sprite_lists()
            self.wall_grid[y][gap] = False

        if wall != 2:
            gap = random.randrange(bottom + 1, y, 2)
            arcade.get_sprites_at_point((x * WALL_WIDTH, gap * WALL_HEIGHT), self.wall_list)[0].remove_from_sprite_lists()
            self.wall_grid[gap][x] = False

        if wall != 3:
            gap = random.randrange(y + 1, top, 2)
            arcade.get_sprites_at_point((x * WALL_WIDTH, gap * WALL_HEIGHT), self.wall_list)[0].remove_from_sprite_lists()
            self.wall_grid[gap][x] = False

        # If there's enough space, make a recursive call
        if top > y + 3 and x > left + 3:
            self.create_maze(top, y, left, x)

        if top > y + 3 and x + 3 < right:
            self.create_maze(top, y, x, right)

        if bottom + 3 < y and x + 3 < right:
            self.create_maze(y, bottom, x, right)

        if bottom + 3 < y and x > left + 3:
            self.create_maze(y, bottom, left, x)

    def grid_to_sprites(self):
        """ Super useful for debugging! """
        for row in range(len(self.wall_grid)):
            for column in range(len(self.wall_grid)):
                if self.wall_grid[row][column]:
                    self.make_wall((MAZE_WIDTH + 1) * WALL_WIDTH + column * WALL_WIDTH, row * WALL_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_list = arcade.SpriteList(use_spatial_hash=False)
        self.wall_list = arcade.SpriteList(use_spatial_hash=False)

        # Set up the player
        self.player_sprite = arcade.Sprite(PLAYER_TEXTURE,
                                           scale=0.5)
        self.player_sprite.center_x = MAZE_WIDTH / 2 * WALL_WIDTH
        self.player_sprite.center_y = MAZE_HEIGHT / 2 * WALL_HEIGHT
        self.player_list.append(self.player_sprite)

        # Initialize the wall grid
        self.wall_grid = tuple([False for x in range(MAZE_WIDTH + 1)] for x in range(MAZE_HEIGHT + 1))

        # Create the map
        self.create_walls()
        self.create_maze(MAZE_HEIGHT, 0, 0, MAZE_WIDTH)

        # Randomly place the coins

        # Create the physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(center_x=self.width // 2,
                                     center_y=20,
                                     width=self.width,
                                     height=40,
                                     color=arcade.color.ALMOND)
        text = f"Player position: ({self.player_sprite.center_x} {self.player_sprite.center_y})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
