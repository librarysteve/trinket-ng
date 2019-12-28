# This script opens notepad and types the msg payload x num_lines        #
# For other keycodes, and documentation on this library check this link: #
# https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html #

####################################################
# Modules imported below must be in the lib folder #
import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

################################################
# Variables below are required for this script #
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)

#####################
# PAYLOAD VARIABLES #
msg = 'I will not leave my computer unlocked when I walk away.'
num_lines = 10

#############
# Functions #
def Open_Notepad():
    kbd.send(Keycode.GUI) ## this is the windows key
    time.sleep(0.80) ## delay bc windows is slow
    layout.write('notepad') ## this is sparta... i mean notepad
    time.sleep(0.80)
    kbd.send(Keycode.ENTER) ## this is the number of times the loop runs
    time.sleep(0.80)

def type_loop(message, lines):
    for times in range(0,lines): 
        layout.write(message)
        kbd.send(Keycode.ENTER)

########
# Main #
Open_Notepad()
type_loop(msg, num_lines)
