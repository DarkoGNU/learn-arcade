import arcade


class MyApplication(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        # Load the sound when the application starts
        self.explosion_sound = arcade.load_sound("laser.wav")
        self.explosion_sound_player = None

    def on_key_press(self, key, modifiers):

        # If the user hits the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


def main():
    window = MyApplication(300, 300)
    arcade.run()


main()
