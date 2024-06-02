from pynput import keyboard
from playsound import playsound
import os

sound_map = {'k':"its_working.wav"}
sound_file_folder = os.path.curdir

def play_sound(keyboardKey):   
        
    path = os.path.join(sound_file_folder,sound_map[keyboardKey])  
    print(path)
    try:
        playsound(path)

    except FileNotFoundError as e:
        print(f"File not found to .wav! {e}")
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == 'k':
            play_sound(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__=="__main__":
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()