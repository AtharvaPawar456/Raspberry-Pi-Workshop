# Reading Digital Input (Button Press):


import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM numbering)
GPIO.setmode(GPIO.BCM)

# Define pin for button input
button_pin = 18

# Set pin as input with pull-down resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            print("Button pressed!")
            # Perform desired action here
            time.sleep(0.2)  # Debounce delay

finally:
    GPIO.cleanup()  # Clean up GPIO on program exit
