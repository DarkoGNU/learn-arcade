from config import *

import random


class MapBuilder:
    def __init__(self, width, height, coin_count):
        """ Konstruktor """
        self.width = width
        self.height = height
        self.coin_count = coin_count

        # Inicjalizuj tablicę z mapą
        self.wall_grid = tuple([False for x in range(self.width + 1)] for x in range(self.height + 1))

        # Inicjalizuj listy sprite'ów
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

    def create_map(self):
        """ Tworzy i zwraca mapę """
        # Stwórz ściany (wall_grid)
        self.create_walls()
        # Stwórz labirynt (wall_grid)
        self.create_maze(self.height, 0, 0, self.width)
        # Przekonwertuj wall_grid na sprite_y
        self.grid_to_sprites()
        # Rozmieść losowo monety
        self.place_coins()

        # Zwróć utworzoną mapę
        return self.wall_list, self.coin_list

    def grid_to_sprites(self):
        """ Konwertuje tabelę 2D na sprite'y """
        for row in range(len(self.wall_grid)):
            for column in range(len(self.wall_grid[row])):
                if self.wall_grid[row][column]:
                    self.make_wall(column * WALL_WIDTH, row * WALL_HEIGHT)

    def create_maze(self, top, bottom, left, right):
        """
        --- Ta funkcja wypełni jedynie tablicę self.wall_grid ---
        Funkcja rekursywna, która dzieli mapę na 4 sekcje i tworzy 3 dziury w powstałych ścianach.
        Labirynt musi mieć nieparzystą liczbę kolumn i wierszy.
        """

        # Oblicz miejsce podziału w poziomie
        start_range = bottom + 2
        end_range = top - 1
        y = random.randrange(start_range, end_range, 2)

        # Dokonaj podziału — postaw ścianę
        for column in range(left + 1, right):
            self.wall_grid[y][column] = True

        # Oblicz miejsce podziału w pionie
        start_range = left + 2
        end_range = right - 1
        x = random.randrange(start_range, end_range, 2)

        # Dokonaj podziału — postaw ścianę
        for row in range(bottom + 1, top):
            self.wall_grid[row][x] = True

        # Zrób dziurę w 3 z 4 powstałych ścian
        # Wylosuj ścianę, w której *nie będzie* dziury
        wall = random.randrange(4)
        if wall != 0:
            gap = random.randrange(left + 1, x, 2)
            self.wall_grid[y][gap] = False

        if wall != 1:
            gap = random.randrange(x + 1, right, 2)
            self.wall_grid[y][gap] = False

        if wall != 2:
            gap = random.randrange(bottom + 1, y, 2)
            self.wall_grid[gap][x] = False

        if wall != 3:
            gap = random.randrange(y + 1, top, 2)
            self.wall_grid[gap][x] = False

        # Jeśli w labiryncie jest wystarczająco wolnej przestrzeni,
        # wywołuj create_maze rekursywnie
        if top > y + 3 and x > left + 3:
            self.create_maze(top, y, left, x)

        if top > y + 3 and x + 3 < right:
            self.create_maze(top, y, x, right)

        if bottom + 3 < y and x + 3 < right:
            self.create_maze(y, bottom, x, right)

        if bottom + 3 < y and x > left + 3:
            self.create_maze(y, bottom, left, x)

    def create_walls(self):
        # Postaw ściany w pionie
        for row in range(self.height):
            self.wall_grid[row][0] = True
            self.wall_grid[row][self.width] = True

        # Postaw ściany w poziomie
        for column in range(self.width + 1):
            self.wall_grid[0][column] = True
            self.wall_grid[self.height][column] = True

    def make_wall(self, center_x, center_y):
        # Wylosuj teksturę
        texture = WALL_TEXTURES[random.randrange(4)]

        # Stwórz ścianę
        self.wall_list.append(arcade.Sprite(
            filename=texture, scale=SPRITE_SCALING,
            center_x=center_x, center_y=center_y))

    def make_coin(self, center_x, center_y):
        # Stwórz pieniążka
        self.coin_list.append(arcade.Sprite(
            filename=COIN_TEXTURE, scale=COIN_SCALING,
            center_x=center_x, center_y=center_y
        ))

    def place_coins(self):
        """ Losowo umieszcza pieniążki w labiryncie """

        # Utwórz pustą listę miejsc, w których zostaną utworzone pieniążki
        empty_places = []

        # Wypełnij listę pustych miejsc
        for row in range(len(self.wall_grid)):
            for column in range(len(self.wall_grid[row])):
                if not self.wall_grid[row][column]:
                    empty_places.append((row, column))

        # Z listy pustych miejsc wylosuj te, gdzie faktycznie zostaną utworzone pieniążki
        coin_locations = random.sample(empty_places, self.coin_count)\
            if len(empty_places) > self.coin_count\
            else empty_places

        # Po kolei utwórz wszystkie pieniążki
        for location in coin_locations:
            self.make_coin(location[1] * WALL_WIDTH, location[0] * WALL_HEIGHT)
