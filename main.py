# This example shows you a simple, non-interrupt way of reading Pico Inky Pack's buttons with a loop that checks to see if buttons are pressed.

import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_INKY_PACK

display = PicoGraphics(display=DISPLAY_INKY_PACK)

# you can change the update speed here!
# it goes from 0 (slowest) to 3 (fastest)
display.set_update_speed(2)

display.set_font("serif")

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)


# a handy function we can call to clear the screen
# display.set_pen(15) is white and display.set_pen(0) is black
def clear():
    display.set_pen(15)
    display.clear()


# set up
clear()
point = "opening"
display.set_pen(0)
display.set_font("serif")
display.text("Welcome Traveler!", 10, 10, 240, 0.5)
display.text("Are you ready to start?", 10, 40, 240, 0.5)
display.set_font("bitmap14_outline")
display.text("A: yes", 50, 80, 240, 1)
display.update()
time.sleep(0.2)

while True:
    if button_a.read():
        if point == "aa":
            clear()
            point = "aaa"
            display.set_pen(0)
            display.set_font("serif")
            display.text("after entering the enemies", 10, 10, 240, 0.5)
            display.text("space station, you hear some", 10, 30, 240, 0.5)
            display.text("footsteps. is it some guards?", 10, 50, 240, 0.5)
            display.set_font("bitmap14_outline")
            display.text("A: hide", 10, 70, 240, 1)
            display.text("B: pull out your gun and prepare to fire", 10, 84, 295, 1)
            display.text("C: confront them", 10, 100, 240, 1)
            display.update()
            time.sleep(0.2)
        if point == "a":
            clear()
            point = "aa"
            display.set_pen(0)
            display.set_font("serif")
            display.text("[here is your stop] the", 10, 10, 240, 0.5)
            display.text("commander tells you and", 10, 30, 240, 0.5)
            display.text("then opens the door", 10, 50, 240, 0.5)
            display.set_font("bitmap14_outline")
            display.text("A: step out", 50, 80, 240, 1)
            display.update()
            time.sleep(0.2)
        if point == "opening" or point == "ab":
            clear()
            point = "a"
            display.set_pen(0)
            display.set_font("serif")
            display.text("The commander looks at you", 10, 10, 240, 0.5)
            display.text("with his stern eyes. [are you", 10, 30, 240, 0.5)
            display.text("ready?] he asks?", 10, 50, 240, 0.5)
            display.set_font("bitmap14_outline")
            display.text("A: yup!", 50, 80, 240, 1)
            display.text("B: what am I supposed to do again?", 50, 95, 240, 1)
            display.update()
            time.sleep(0.2)
            
    elif button_b.read():
        if point == "a":
            clear()
            point = "ab"
            display.set_pen(0)
            display.set_font("serif")
            display.text("[we've been over this 1000]", 10, 10, 240, 0.5)
            display.text("times, you have to disable", 10, 30, 240, 0.5)
            display.text("power to the enemy base]", 10, 50, 240, 0.5)
            display.set_font("bitmap14_outline")
            display.text("A: I remember now", 50, 80, 240, 1)
            display.update()
            time.sleep(0.2)
    elif button_c.read():
        clear()
        display.set_pen(0)
        display.text("Button C pressed", 10, 90, 240, 3)
        display.update()
        time.sleep(0.5)
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses
