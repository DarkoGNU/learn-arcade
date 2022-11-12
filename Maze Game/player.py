from config import *

import arcade

# Kierunek, w który zwrócona jest postać gracza
RIGHT_FACING = 0
LEFT_FACING = 1


class Player(arcade.Sprite):
    """ Reprezentuje gracza """

    @staticmethod
    def load_texture_pair(texture):
        """ Ładuje parę tekstur — zwróconą w prawo i zwróconą w lewo """
        return (
            arcade.load_texture(texture),
            arcade.load_texture(texture, flipped_horizontally=True)
        )

    def __init__(self):
        """ Konstruktor """

        # Wywołaj konstruktor superklasy
        super().__init__()

        # Wciśnięte klawisze
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Domyślnie postać zwrócona w prawo
        self.character_face_direction = RIGHT_FACING

        # Śledź number obecnej tekstury
        self.cur_texture = 0
        # Ustaw skalę
        self.scale = PLAYER_SCALING

        # Załaduj tekstury do stania w miejscu
        self.idle_texture_pair = self.load_texture_pair(f"{PLAYER_TEXTURE}_idle.png")

        # Załaduj tekstury do chodzenia
        self.walk_textures = []
        for i in range(8):
            texture = self.load_texture_pair(f"{PLAYER_TEXTURE}_walk{i}.png")
            self.walk_textures.append(texture)

        # Ustaw teksturę początkową
        self.texture = self.idle_texture_pair[0]

        # Ustaw hitbox
        self.hit_box = self.texture.hit_box_points

    def update_animation(self, delta_time: float = 1 / 60):
        """ Aktualizuje teksturę gracza """

        # Sprawdź, czy nie ma potrzeby zmiany orientacji tekstury
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Tekstura stania w miejscu
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Animacja chodzenia
        self.cur_texture += 1
        if self.cur_texture // 3 > 7:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture // 3][
            self.character_face_direction
        ]

    def on_update(self, delta_time: float = 1 / 60):
        """ Aktualizuje prędkość gracza """

        # Szybkość w pionie
        if self.up_pressed and not self.down_pressed:
            self.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.change_y = -PLAYER_MOVEMENT_SPEED
        else:
            self.change_y = 0

        # Szybkość w poziomie
        if self.left_pressed and not self.right_pressed:
            self.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_x = PLAYER_MOVEMENT_SPEED
        else:
            self.change_x = 0

        # Wywołaj funkcję superklasy
        super().on_update(delta_time)
