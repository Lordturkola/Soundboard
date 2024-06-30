from pynput import keyboard
import pygame

import os

sound_map = {
    "k": "its_working.wav",
    "n": "no_darth.wav",
    "v": "varskrik.wav",
    "b": "bbbad.wav",
    "f": "lotr_br_q.wav",
    "c": "cmon.wav",
    "h": "hastalavista_trimmed.wav",
    "w": "whatgoingon.wav",
    "g": "goood.wav",
    "r": "rockapa.wav",
    "i": "iwanttobreakfree.wav",
    "d": "doit.mp3",
}
sound_file_folder = os.path.curdir


def play_sound(keyboardKey):

    try:
        path = os.path.join(sound_file_folder, sound_map[keyboardKey])
        print(path)
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    except FileNotFoundError as e:
        print(f"File not found to .wav! {e}")
    except KeyError as e2:
        print(f"No binding for pressed key: {keyboardKey}")


def on_press(key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
        play_sound(key.char)
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == "__main__":
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
