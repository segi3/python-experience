from pyautogui import *
import pyautogui as pyg
import time
import keyboard
import random
import win32api, win32con

#tile 1 x=547 y=400
#tile 2 x=627 y=400
#tile 3 x=712 y=400
#tile 4 x=804 y=400

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    
    if pyg.pixel(547, 400)[0] == 0:
        click(547, 400)
    if pyg.pixel(627, 400)[0] == 0:
        click(627, 400)
    if pyg.pixel(712, 400)[0] == 0:
        click(712, 400)
    if pyg.pixel(804, 400)[0] == 0:
        click(804, 400)
    
    # if (pyg.pixel(547, 400)[0] + pyg.pixel(547, 400)[1] + pyg.pixel(547, 400)[2]) == 0:
    #     click(547, 400)
    # if (pyg.pixel(627, 400)[0] + pyg.pixel(627, 400)[1] + pyg.pixel(627, 400)[2]) == 0:
    #     click(627, 400)
    # if (pyg.pixel(712, 400)[0] + pyg.pixel(712, 400)[1] + pyg.pixel(712, 400)[2]) == 0:
    #     click(712, 400)
    # if (pyg.pixel(804, 400)[0] + pyg.pixel(804, 400)[1] + pyg.pixel(804, 400)[2]) == 0:
    #     click(804, 400)

