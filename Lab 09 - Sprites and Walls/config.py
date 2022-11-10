# For calculating wall's size
from arcade import Sprite

PLAYER_SCALING = 0.5
SPRITE_SCALING = 0.5
COIN_SCALING = 0.25

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7

# Sprite textures
PLAYER_TEXTURE = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
WALL_TEXTURES = (":resources:images/tiles/dirtCenter.png", ":resources:images/tiles/planetCenter.png",
                 ":resources:images/tiles/stoneCenter.png", ":resources:images/tiles/snowCenter.png")
COIN_TEXTURE = ":resources:images/items/coinGold.png"

# Maze must have an ODD number of rows and columns.
# Walls go on EVEN rows/columns.
# Openings go on ODD rows/columns
MAZE_HEIGHT = 17
MAZE_WIDTH = 17

# Coin count
COIN_COUNT = 50

# Sounds
MUSIC = ":resources:music/1918.mp3"
COIN_SOUND = ":resources:sounds/coin2.wav"

# Wall height and width
WALL_HEIGHT = Sprite(WALL_TEXTURES[0], SPRITE_SCALING).height
WALL_WIDTH = Sprite(WALL_TEXTURES[0], SPRITE_SCALING).width

# Revert the import
del Sprite
