import pyautogui as pyg
import time

f = open("bee_movie.txt", 'r')

count = 0;

for word in f:
    if count == 2000:
        break
    print(word + ' ' + str(count))
    pyg.typewrite(word)
    pyg.press("enter")
    count=count+1