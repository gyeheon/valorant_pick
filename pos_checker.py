import pyautogui
import time 
import keyboard

while 1:
    if keyboard.read_key() == "space":
        position = pyautogui.position()
        print(position.x, position.y)
        time.sleep(0.5)
