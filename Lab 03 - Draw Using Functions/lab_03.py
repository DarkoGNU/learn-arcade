import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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


def on_draw(delta_time):
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

    # Draw a moving sun
    draw_sun(on_draw.sun_x_pos, 500)

    # Change Sun's position
    on_draw.sun_x_pos += 3
    if (on_draw.sun_x_pos > SCREEN_WIDTH + 50):
        on_draw.sun_x_pos = -50

    arcade.finish_render()


on_draw.sun_x_pos = 300


def main():
    arcade.open_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

    arcade.schedule(on_draw, 1/60)
    arcade.run()


if __name__ == "__main__":
    main()
