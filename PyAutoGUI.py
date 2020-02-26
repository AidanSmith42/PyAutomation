import pyautogui
import time
from datetime import datetime

print(pyautogui.size())

i=1
print("")
print("")
print("This will press the space button every minute in order to keep your computer active")


print("Type ctrl C to quit, or close the cmd prompt")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
while i ==1:

	time.sleep(1)
	pyautogui.press('space')
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	time.sleep(59) 	 