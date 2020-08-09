from pyautogui import *
import pyautogui as pyg
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print("start")
while keyboard.is_pressed('q') == False:

    pic = pyg.screenshot(region=(90, 417, 780, 570))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            print(r, g, b)
            if b == 195:
                click(x+90, y+417)
                time.sleep(0.5)
                break

print("exit")


