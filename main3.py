import tkinter as tk
from playsound import playsound
import os
import keyboard
 
sound_map = {"k":"its_working.wav"}

def play_sound(keyboardKey):   
    path = os.path.join(os.path.curdir,sound_map[keyboardKey])  
    print(path)
    try:
        playsound(path)

    except FileNotFoundError as e:
        print(f"File not found to .wav! {e}")

if __name__=="__main__":
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            play_sound(event.name)
