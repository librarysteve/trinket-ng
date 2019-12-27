import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)
kbd.send(Keycode.GUI)
time.sleep(0.2)
layout.write('notepad')
time.sleep(1.0)
kbd.send(Keycode.ENTER)
time.sleep(0.5)
for times in range(0,9):
    layout.write('I will not leave my computer unlocked')
    time.sleep(0.05)
    kbd.send(Keycode.ENTER)

exit()


## For other keycodes, and documentation on this library check this link:
## https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html
