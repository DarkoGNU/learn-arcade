"""
Gra — zbieranie pieniążków w labiryncie.

Labirynt jest generowany losowo, tak samo, jak ułożenie pieniążków.
"""
from pyglet.math import Vec2

from maze_gen import *
from player import *


class MyGame(arcade.Window):
    """ Główna klasa gry. """

    def __init__(self, width, height, title):
        """ Konstruktor """

        # Wywołaj konstruktor superklasy
        super().__init__(width, height, title, resizable=True)

        # Ukryj kursor
        self.set_mouse_visible(False)

        # Listy sprite'ów
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Zmienna przechowująca gracza
        self.player = None

        # Zmienna przechowująca wynik
        self.score = 0

        # Zmienna przechowująca numer levelu
        self.level = 0

        # Zmienna przechowująca stan gry
        self.game_over = False

        # Silnik fizyczny — zapobiega przechodzeniu przez ściany
        self.physics_engine = None

        # Kamery
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Dźwięki
        self.music = arcade.load_sound(MUSIC)
        self.music_player = None
        self.coin_sound = arcade.load_sound(COIN_SOUND)

    def setup(self):
        """ Inicjalizuj grę """

        # Utwórz listę sprite'ów dla gracza
        self.player_list = arcade.SpriteList(use_spatial_hash=False)

        # Utwórz mapę
        self.wall_list, self.coin_list = MapBuilder(
            MAZE_WIDTH[self.level], MAZE_HEIGHT[self.level], COIN_COUNT[self.level]
             ).create_map()

        # Stwórz gracza
        self.player = Player()
        self.player.center_x = MAZE_WIDTH[self.level] / 2 * WALL_WIDTH
        self.player.center_y = MAZE_HEIGHT[self.level] / 2 * WALL_HEIGHT
        self.player_list.append(self.player)

        # Zresetuj wynik, jeśli level == 1
        if self.level == 0:
            self.score = 0

        # Zresetuj status
        self.game_over = False

        # Utwórz silnik fizyczny
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)

        # Uruchom muzykę
        if not self.music_player or not self.music_player.playing:
            self.music_player = self.music.play(volume=0.2, loop=True)

        # Ustaw kolor tła
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Renderuje grę """

        # Sprawdź, czy gra nie jest zakończona
        if self.game_over:
            self.clear(arcade.color.BLACK)
            arcade.draw_text(
                f"Koniec gry. Ostateczny wynik: {self.score}",
                self.width / 2,
                self.height / 2,
                arcade.color.WHITE,
                30,
                anchor_x="center"
            )
            return

        # Rozpocznij render
        arcade.start_render()

        # Użyj kamery dla sprite'ów
        self.camera_sprites.use()

        # Narysuj wszystkie sprite'y
        for sprites in self.wall_list, self.coin_list, self.player_list:
            sprites.draw()

        # Użyj kamery dla GUI
        self.camera_gui.use()

        # Narysuj GUI
        arcade.draw_rectangle_filled(center_x=self.width // 2,
                                     center_y=20,
                                     width=self.width,
                                     height=40,
                                     color=arcade.color.ALMOND)
        text = f"Wynik: {self.score}, " \
               f"Pozostało: {len(self.coin_list)} pieniążków"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """ Obsłuż wciśnięcie klawisza """

        if key == arcade.key.UP:
            self.player.up_pressed = True
        elif key == arcade.key.DOWN:
            self.player.down_pressed = True
        elif key == arcade.key.LEFT:
            self.player.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.player.right_pressed = True

    def on_key_release(self, key, modifiers):
        """ Obsłuż zwolnienie klawisza """

        if key == arcade.key.UP:
            self.player.up_pressed = False
        elif key == arcade.key.DOWN:
            self.player.down_pressed = False
        elif key == arcade.key.LEFT:
            self.player.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.player.right_pressed = False

    def on_update(self, delta_time):
        """ Logika gry """

        # Sprawdź, czy wszystkie pieniążki są zebrane
        if len(self.coin_list) <= 0:
            if self.level + 1 < LEVEL_COUNT:
                # Idź na kolejny level
                self.level += 1
                # Inicjalizuj grę od nowa (wynik zostanie zachowany)
                self.setup()
                # Natychmiast scrolluj kamerę do gracza
                self.scroll_to_player(1)
            else:
                self.game_over = True

            return

        # Aktualizuj wszystkie sprite'y
        self.player.on_update(delta_time)
        self.physics_engine.update()
        self.player_list.update_animation()

        # Scrolluj kamerę do gracza
        self.scroll_to_player()

        # Sprawdź, czy gracz zebrał jakieś pieniążki
        coin_hits = arcade.check_for_collision_with_list(self.player, self.coin_list)

        # Dla każdego zebranego pieniążka
        for hit in coin_hits:
            self.score += 1
            hit.remove_from_sprite_lists()
            self.coin_sound.play()

    def scroll_to_player(self, camera_speed=CAMERA_SPEED):
        """ Scrolluje kamerę do pozycji gracza """

        # Oblicz pozycję kamery
        position = Vec2(self.player.center_x - self.width / 2,
                        self.player.center_y - self.height / 2)
        # Przesuń kamerę
        self.camera_sprites.move_to(position, camera_speed)

    def on_resize(self, width, height):
        """ Zmień rozmiar okna """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Funkcja main """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


# Wywołaj funkcję main
if __name__ == "__main__":
    main()
