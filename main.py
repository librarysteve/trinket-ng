# This script opens notepad and types the msg payload x num_lines        #
# For other keycodes, and documentation on this library check this link: #
# https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html #
#       For my colleagues...                                             #
#                       - m3lodicmin0r                                   #

####################################################
# Modules imported below must be in the lib folder #
import time
import board
import digitalio
import adafruit_dotstar as dotstar
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


################################################
# Variables below are required for this script #
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)
dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1.0)


#############
# Color Def #
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
OFF = (0, 0, 0)


#####################
# Payload Variables #
msg = 'I will not leave my computer unlocked when I walk away.'
num_lines = 5


#############
# Functions #
def flash_color(times, color, del_spd):
    for i in range(0,times):
        dots[0] = (color)
        time.sleep(del_spd)
        dots[0] = (OFF)
        time.sleep(del_spd)

def Open_Notepad():
    kbd.send(Keycode.GUI)   ## this is the windows key
    time.sleep(0.80)
    layout.write('notepad') ## this is sparta... i mean notepad
    time.sleep(0.80)
    kbd.send(Keycode.ENTER) ## this is the number of times the loop runs
    time.sleep(0.80)

def type_loop(message, lines):
    for times in range(0,lines): 
        layout.write(message)
        kbd.send(Keycode.ENTER)
        flash_color(2, MAGENTA, 0.01)


###################
# Execute Program #
flash_color(1, OFF, 1.5)    # The LED will blink CYAN when starting the program
flash_color(1, CYAN, 1)     # flash MAGENTA while the HID injection is happening
Open_Notepad()              # then rapidly flash BLUE to signal the end of the program
type_loop(msg, num_lines)
time.sleep(1.0)
flash_color(12, BLUE, 0.05)


###############################################
# Turn the LED off forever un till you unplug #
while True:
    dots[0] = (OFF)
