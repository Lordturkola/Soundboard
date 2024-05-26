from pynput import keyboard
def fetchAudioSamples():
    pass
def playAudioSample(sample):
    pass 
def initalize():
    pass     
def on_press(key):
    try:
        print(f"alphanum key {key.char}")
    except AttributeError:
        print(f"special key pressed {key}")

with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

if __name__=="__main__":
        
    pass