"""
A drawing in Arcade
"""

# Import "arcade"
import arcade

# Open a window
arcade.open_window(width=800, height=600, window_title="My drawing")

# Set background color
arcade.set_background_color((52, 227, 221))

# Start rendering
arcade.start_render()

# Make some grass
arcade.draw_lrtb_rectangle_filled(top=150, bottom=0, left=0, right=800, color=arcade.csscolor.GREEN)

# Make some dirt
arcade.draw_lrtb_rectangle_filled(top=50, bottom=0, left=0, right=800, color=arcade.color.DARK_BROWN)

# Draw a skeleton
arcade.draw_line(start_x=50, start_y=30, end_x=100, end_y=15, color=arcade.csscolor.GRAY, line_width=5)
arcade.draw_line(start_x=50, start_y=0, end_x=100, end_y=15, color=arcade.csscolor.GRAY, line_width=5)
arcade.draw_line(start_x=100, start_y=15, end_x=130, end_y=15, color=arcade.csscolor.GRAY, line_width=5)
arcade.draw_line(start_x=100, start_y=40, end_x=120, end_y=15, color=arcade.csscolor.GRAY, line_width=5)
arcade.draw_line(start_x=100, start_y=-10, end_x=120, end_y=15, color=arcade.csscolor.GRAY, line_width=5)
arcade.draw_circle_outline(center_x=140, center_y=15, radius=15, color=arcade.csscolor.GRAY, border_width=5)

# Draw a basic tree
arcade.draw_rectangle_filled(center_x=400, center_y=200, width=20, height=100, color=arcade.csscolor.SIENNA)
arcade.draw_circle_filled(center_x=400, center_y=300, radius=50, color=arcade.csscolor.GREEN)

# Draw another tree
arcade.draw_lrtb_rectangle_filled(left=100, right=130, bottom=150, top=200, color=arcade.csscolor.DARK_KHAKI)
arcade.draw_arc_filled(center_x=115, center_y=200, width=100, height=100, start_angle=-10, end_angle=190,
                       color=arcade.csscolor.DARK_GREEN)

# Draw a cloud
arcade.draw_polygon_filled(((500, 500), (520, 530), (530, 569), (560, 590), (500, 600), (400, 500), (420, 543)),
                           color=arcade.csscolor.LIGHT_GRAY)

# Draw a sun
arcade.draw_circle_filled(center_x=100, center_y=500, radius=50, color=arcade.csscolor.YELLOW)
arcade.draw_line(start_x=100, end_x=100, start_y=590, end_y=410, color=arcade.csscolor.YELLOW, line_width=3)
arcade.draw_line(start_x=10, end_x=190, start_y=500, end_y=500, color=arcade.csscolor.YELLOW, line_width=3)
arcade.draw_line(start_x=50, end_x=150, start_y=550, end_y=450, color=arcade.csscolor.YELLOW, line_width=3)
arcade.draw_line(start_x=150, end_x=50, start_y=550, end_y=450, color=arcade.csscolor.YELLOW, line_width=3)

# Draw a flag with text
arcade.draw_polygon_outline(((315, 150), (330, 150), (330, 250), (270, 250), (270, 220), (315, 220)),
                            color=arcade.csscolor.BLACK)
arcade.draw_text(start_x=285, start_y=230, text="Hey!", color=arcade.csscolor.BLACK, font_size=15)

# Finish rendering
arcade.finish_render()

# Show until the window is closed
arcade.run()
