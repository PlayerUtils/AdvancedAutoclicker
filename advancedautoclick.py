#Do not touch anything without a comment next to it if you do not know what you are doing!!

import pyautogui
import time
import random
import keyboard

clicks = 0
closeOnMax = True #Wether it should close on max clicks, set it to 'False' (case sensitive) if you want it to close on max clicks
delay = 1  #The average delay of the autoclick you want
randomness = 0.5  #The randomness (how many seconds before or after the average delay it will randomly click) of the delay
holdTime = 0.3 #The time the mouse will be held down for
maxClicks = 99999999 #How many total clicks you wish to do

activationKey = 'f2' #Activation keys ie 'f1' 'esc' 'tab' '`'
# DO NOT PUT E, IT WILL ALSO ENABLE DEBUG!

# DO NOT TOUCH! THIS SENDS ON SCRIPT OPEN
print("//////////////////////////////////////////")
print("Advanced AutoClicker")
print("OPEN FILE FOR SETTINGS")
print(f"Press {activationKey} to start!")
print(f"Configs:\nDelay: {delay}\nRandomness: {randomness}\nMouse-Hold-Time: {holdTime}")
print("Press E for debug")
print("//////////////////////////////////////////")
#You can now touch anything below with a comment.
# FOR NEW PYTHON USERS - CTRL + S TO SAVE, OR IT WONT UPDATE!
autoclickerActivated = False

def toggleAutoclicker(event):
    global clicks
    clicks = 0
    global autoclickerActivated
    autoclickerActivated = not autoclickerActivated

def debug(event):
    x, y = pyautogui.position()
    print(x, y)

keyboard.on_press_key(activationKey, toggleAutoclicker)
keyboard.on_press_key('e', debug)


while True:
    while True:
            if autoclickerActivated:
                x, y = pyautogui.position()

                pyautogui.mouseDown()
                time.sleep(holdTime) 
                pyautogui.mouseUp()
                clicks = clicks + 1

                time.sleep(delay + random.uniform(-randomness, randomness))
                if clicks >= maxClicks:
                    if closeOnMax:
                         toggleAutoclicker()
                    else:
                         autoclickerActivated = False
#For more utils please visit https://github.com/PlayerUtils/
