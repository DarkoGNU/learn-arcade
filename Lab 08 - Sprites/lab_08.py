import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_SPRITE = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
GOOD_SPRITE = ":resources:images/tiles/mushroomRed.png"
BAD_SPRITE = ":resources:images/tiles/bomb.png"

PLAYER_SPRITE_SCALE = 0.6
GOOD_SPRITE_SCALE = 0.3
BAD_SPRITE_SCALE = 0.15

SPRITE_COUNT = 50

SPRITE_SPEED = 1


class MyGame(arcade.Window):
    """ Our custom Window Class """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.bad_list = None
        self.good_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.game_over = False

        # Sounds
        self.good_sound = None
        self.good_sound_player = None
        self.bad_sound = None
        self.bad_sound_player = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def play_good_sound(self):
        if not self.good_sound_player or not self.good_sound_player.playing:
            self.good_sound_player = self.good_sound.play()

    def play_bad_sound(self):
        if not self.bad_sound_player or not self.bad_sound_player.playing:
            self.bad_sound_player = self.bad_sound.play()

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()

        # Sounds
        self.good_sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.good_sound_player = None
        self.bad_sound = arcade.load_sound(":resources:sounds/error4.wav")
        self.bad_sound_player = None

        # Score
        self.score = 0

        # Game state
        self.game_over = False

        # Set up the player
        self.player_sprite = arcade.Sprite(PLAYER_SPRITE, PLAYER_SPRITE_SCALE)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the good and bad sprites
        for i in range(SPRITE_COUNT):
            # Create both sprite instances
            good_sprite = arcade.Sprite(GOOD_SPRITE, GOOD_SPRITE_SCALE)
            bad_sprite = arcade.Sprite(BAD_SPRITE, BAD_SPRITE_SCALE)

            # Position the good sprite
            good_sprite.center_x = random.randrange(SCREEN_WIDTH)
            good_sprite.center_y = random.randrange(SCREEN_HEIGHT)

            # Position the bad sprite
            bad_sprite.center_x = random.randrange(SCREEN_WIDTH)
            bad_sprite.center_y = random.randrange(SCREEN_HEIGHT)

            # Add them to the sprite lists
            self.good_list.append(good_sprite)
            self.bad_list.append(bad_sprite)

    def on_draw(self):
        """ Draw everything. """
        arcade.start_render()

        if self.game_over:
            self.clear(arcade.color.BLACK)
            arcade.draw_text("Game over!",
                             SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2,
                             arcade.color.WHITE, 30, anchor_x="center")
            arcade.draw_text(f"Final score: {self.score}",
                             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40,
                             arcade.color.WHITE, 30, anchor_x="center")
            return

        for sprites in self.player_list, self.good_list, self.bad_list:
            sprites.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        if self.game_over:
            return

        # Move the center of the player sprite to match the mouse's x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def move_good_sprites(self):
        for sprite in self.good_list:
            sprite.center_y -= SPRITE_SPEED

            if sprite.top < 0:
                sprite.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 300)
                sprite.center_x = random.randrange(SCREEN_WIDTH)

    def move_bad_sprites(self):
        for sprite in self.bad_list:
            sprite.center_y += SPRITE_SPEED

            if sprite.bottom > SCREEN_HEIGHT:
                sprite.top = random.randrange(-300, 0)
                sprite.center_x = random.randrange(SCREEN_WIDTH)

            sprite.center_x -= SPRITE_SPEED

            if sprite.right < 0:
                sprite.right = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 300)
                sprite.center_y = random.randrange(SCREEN_HEIGHT)

    def update(self, delta_time):
        """ Movement and game logic """

        if len(self.good_list) <= 0:
            self.game_over = True
            return

        # Call update on all sprites (The sprites don't do much in this
        # example though).
        for sprites in self.player_list, self.good_list, self.bad_list:
            sprites.update()

        # Move the sprites
        self.move_good_sprites()
        self.move_bad_sprites()

        # Generate a list of all good sprites that collided with the player
        good_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_list)
        # Generate a list of all bad sprites that collided with the player
        bad_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_list)

        # Remove good sprites and increment the score
        for hit in good_list:
            hit.remove_from_sprite_lists()
            self.score += 1
            self.play_good_sound()

        # Remove bad sprites and increment the score
        for hit in bad_list:
            hit.remove_from_sprite_lists()
            self.score -= 1
            self.play_bad_sound()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
