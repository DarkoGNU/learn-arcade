"""
Recursive H's
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

RECURSION_DEPTH = 10


def draw_h(x, y, width, height, count):
    """ Recursively draw an H, each one half as big """

    # Cached variables
    count -= 1
    height_d_2 = height * .5
    height_d_2_p_y = height_d_2 + y
    y_p_height_t_025 = y + height * .25
    y_p_height_t_075 = y + height * .75
    y_p_height_d_2 = y + height_d_2
    width_d_2 = width * .5
    x_p_width_t_025 = x + width * .25
    x_p_width_t_075 = x + width * .75
    x_p_width_d_2 = x + width_d_2


    # Draw the H
    # Draw cross-bar
    arcade.draw_line(x_p_width_t_025, height_d_2_p_y,
                     x_p_width_t_075, height_d_2_p_y,
                     arcade.color.BLACK)

    # Draw left side
    arcade.draw_line(x_p_width_t_025, y_p_height_t_025,
                     x_p_width_t_025, y_p_height_t_075,
                     arcade.color.BLACK)

    # Draw right side
    arcade.draw_line(x_p_width_t_075, y_p_height_t_025,
                     x_p_width_t_075, y_p_height_t_075,
                     arcade.color.BLACK)

    # As long as count is greater than 0, recursively call this function with a smaller H
    if count > 0:
        # Draw lower left
        draw_h(x, y, width_d_2, height_d_2, count)
        # Draw lower right
        draw_h(x_p_width_d_2, y, width_d_2, height_d_2, count)
        # Draw upper left
        draw_h(x, y_p_height_d_2, width_d_2, height_d_2, count)
        # Draw upper right
        draw_h(x_p_width_d_2, y_p_height_d_2, width_d_2, height_d_2, count)


class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Start our recursive calls
        draw_h(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, RECURSION_DEPTH)


def main():
    MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
