import pyautogui as pyg
import time

f = open("words.txt", 'r')

for word in f:
    print(word)
    pyg.typewrite(word)
    pyg.press("enter")