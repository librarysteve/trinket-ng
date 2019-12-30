# trinket-ng
*next gen? national geographic? ninja gaiden?*
<!-- hacktheplanet! -->

### We-pwn-izing the Adafruit Trinket M0 for fun and profit.
### (but mostly for some people I work with :space_invader: )

## Use Cases:
* *remind* someone to lock thier workstation
* Automate a repetative task across air gapped devices
* Look like a hacker
* Send keystrokes or mouse clicks at super humans speeds!


## Setup:
1. To run the example, replace the content of the main.py file on the board with [this](https://github.com/librarysteve/trinket-ng/blob/master/main.py)
2. Edit the peyload variables to your liking (or leave it as is)
3. Save and be ready for that paylod to run. It will run immediately.

----------------------------------------------------------------------------------------

The LED will flash __CYAN__ to signal the start of the program,

then flash __MAGENTA__ while executing,

and rapidly flash __BLUE__ to signal the end.

*\*the led will dim up and down GREEN after the program runs to signal that it can be reprogeammed.*

-----------------------------------------------------------------------------------------

Suggested editors are: 
* mu
https://codewith.mu/ (this intigrates with the board and will give you errors in the serial console)

* notepad
* nano (Linux/OSX)
* vim (if you hate life)
* emacs (if youre a wizzard)
###### Notepad++ is not recommended due to the way it saves files in session.

-----------------------------------------------------------------------------------------

#### Note:
Use the zipped library [here](https://github.com/librarysteve/trinket-ng/blob/master/lib.zip) to make sure you have all the required modules.
Unzip and drag it into the same foler as the main.py file.

Direcotry for lib should look like:

CIRCUITPY:\lib\adafruit_dotstar.mpy

CIRCUITPY:\lib\adafruit_hid\ (the other .mpy files)
