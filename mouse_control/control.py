from pynput.keyboard import Key, Listener
import pyautogui
import sys
from threading import Thread

exit_key = False

def on_press(key):
    #print('{0} pressed'.format(key))
    print('')

def on_release(key):
    #print('{0} release'.format(key))`
    if key == Key.esc:
        global exit_key
        exit_key = True
        #Stop listener
        sys.exit()

def listen_key():
    print("Press 'ESC' to exit")
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def get_position():
    thread1 = Thread(target=listen_key, args=())
    thread1.start()
    while True:
        #print(pyautogui.position())
        x, y = pyautogui.position()
        sys.stdout.write("\rmouse position x = {} y = {}".format(x, y))
        global exit_key
        if exit_key:
            break
    thread1.join()
    print('')