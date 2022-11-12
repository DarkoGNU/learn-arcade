# Potrzebne do wyliczenia wymiarów ściań
import arcade

# Skale sprite'ów
PLAYER_SCALING = 0.5
SPRITE_SCALING = 0.5
COIN_SCALING = 0.25

# Ustawienia okna
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Labirynt"

# Kamera — minimalny margines pomiędzy graczem i krawędzią okna
VIEWPORT_MARGIN = 220

# Szybkość przesuwania kamery
CAMERA_SPEED = 0.1

# Szybkość gracza
PLAYER_MOVEMENT_SPEED = 7

# Tekstury sprite'ów
PLAYER_TEXTURE = ":resources:images/animated_characters/male_person/malePerson"
WALL_TEXTURES = (":resources:images/tiles/dirtCenter.png", ":resources:images/tiles/planetCenter.png",
                 ":resources:images/tiles/stoneCenter.png", ":resources:images/tiles/snowCenter.png")
COIN_TEXTURE = ":resources:images/items/coinGold.png"

# Liczba poziomów
LEVEL_COUNT = 3

# Rozmiar labiryntu dla każdego levelu. Ilość wierszy i kolumn **musi być nieparzysta**
MAZE_HEIGHT = (9, 17, 21)
MAZE_WIDTH = (9, 17, 21)

# Liczba pieniążków dla każdego levelu
COIN_COUNT = (25, 50, 75)

# Dźwięki
MUSIC = ":resources:music/1918.mp3"
COIN_SOUND = ":resources:sounds/coin2.wav"

# Wysokość i szerokość ścian
WALL_HEIGHT = arcade.Sprite(WALL_TEXTURES[0], SPRITE_SCALING).height
WALL_WIDTH = arcade.Sprite(WALL_TEXTURES[0], SPRITE_SCALING).width
