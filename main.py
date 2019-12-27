import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)
kbd.send(Keycode.GUI)  ## this is the windows key
time.sleep(0.1)
layout.write('notepad') ## this is sparta... i mean notepad
time.sleep(0.1)
kbd.send(Keycode.ENTER)
time.sleep(0.2)
for times in range(0,9): ## this is the number of times the loop runs
    layout.write('I will not leave my computer unlocked') ## This will be typed into notepad
    time.sleep(0.01)
    kbd.send(Keycode.ENTER)
    
exit()

## For other keycodes, and documentation on this library check this link:
## https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html
