from pynput import keyboard
import vlc
from time import sleep


class MediaManager:
    def __init__(self):
        self.media_key_map = {
            "f": "C:\\Users\\andre\\GIT_PROJECTS_FUUUCK\\Soundboard\\media\\f\\media_file_f.webm"
        }
        self.media_instance = vlc.Instance(["--video-on-top"])
        self.media_player = self.media_instance.media_player_new()
        self.media_player.set_fullscreen(True)
        self.playing = False

    def play_media(self, key):
        self.playing = True
        try:
            media = self.media_instance.media_new(self.media_key_map[key])
            self.media_player.set_media(media)
            events = self.media_player.event_manager()
            events.event_attach(
                vlc.EventType.MediaPlayerEndReached,
                self.stop_media,
            )
            self.media_player.play()
            while self.playing:
                sleep(0.5)
        except FileNotFoundError as e:
            print(f"File not found to media file {e}")
        except KeyError as e2:
            print(f"No binding for pressed key: {key}")
        finally:
            print("finally stopping video")
            self.stop_media(vlc.EventType.MediaPlayerEndReached)

    def start_screen(self, key):
        pass

    def on_press(self, key):
        try:
            str_key = str(key.char)
            print("key pressed {0}".format(key.char))
            print(self.media_key_map)
            print(self.media_key_map.get(str_key, None))
            if not self.playing and self.media_key_map.get(str_key, None) != None:
                self.play_media(str_key)
        except AttributeError:
            print("special key {0} pressed".format(key))

    def stop_media(self, event):
        print("stopping video")
        self.playing = False
        self.media_player.stop()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            # stop video prematurely
            return False

    def listen_to_keypress(self):
        # Collect events until released
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()


if __name__ == "__main__":
    mm = MediaManager()
    mm.listen_to_keypress()
