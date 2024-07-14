from pynput import keyboard
import vlc
from time import sleep
from threading import Thread
from pipeline.pipelineItems.model.mediaItem import MediaItem


class MediaManager:
    def __init__(self):
        self.media_key_map = {
            "f": "C:\\Users\\andre\\GIT_PROJECTS_FUUUCK\\Soundboard\\media\\f\\media_file_f.webm",
            "b": "C:\\Users\\andre\\GIT_PROJECTS_FUUUCK\\Soundboard\\media\\b\\media_file_b.webm",
        }
        self.media_instance = vlc.Instance(
            ["--video-on-top", "--play-and-exit", "vlc://quit", "--play-and-stop"]
        )
        self.media_player = self.media_instance.media_player_new()
        self.media_player.set_fullscreen(True)
        self.media_player.video_set_key_input(True)
        self.playing = False

    def play_media(self, key):
        self.playing = True
        try:
            media = self.media_instance.media_new_path(self.media_key_map[key])
            self.media_player.set_media(media)

            events = self.media_player.event_manager()
            events.event_attach(vlc.EventType.MediaPlayerEndReached, self.stop_media)
            events.event_attach(
                vlc.EventType.MediaPlayerEncounteredError, self.stop_media
            )

            self.media_player.play()
            while self.playing:
                print("is playing")
                sleep(0.5)
        except Exception as e:
            print(f"an error {e} occured whie trying to play")
        finally:
            print("finally stopping video")
            self.stop_media(vlc.EventType.MediaPlayerEndReached)

    def stop_media(self, event):
        print("stopping video")
        self.playing = False

    def on_press(self, key):
        try:
            str_key = str(key.char)
            print("key pressed {0}".format(key.char))
            # print(self.media_key_map)
            print(self.playing)
            if not self.playing and self.media_key_map.get(str_key, None) != None:
                print("starting task")
                task = Thread(target=self.play_media, args=(str_key,))
                task.start()
        except AttributeError:
            print("special key {0} pressed".format(key))

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            # stop video prematurely
            return False

    def update(self, mediaItem: MediaItem):
        self.media_key_map[mediaItem.key_bindning] = mediaItem.file_path

    def start(self):
        # Collect events until released
        with keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()


if __name__ == "__main__":
    mm = MediaManager()
    mm.start()
