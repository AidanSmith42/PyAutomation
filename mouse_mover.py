import pyautogui
import time
from datetime import datetime

print(pyautogui.size())

i=1;
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
while i == 1:

	time.sleep(1)
	pyautogui.keyDown('left')
	time.sleep(.113)
	pyautogui.keyUp('right')
	pyautogui.click(x=1850, y=680)
	time.sleep(30)
	pyautogui.press('space')
	time.sleep(2) 	
	time.sleep(10)  
