import pyautogui as pg 
import time

time.sleep(5)
for i in range(100):
	pg.write('hello world')
	time.sleep(0.05)
	pg.press('Enter')