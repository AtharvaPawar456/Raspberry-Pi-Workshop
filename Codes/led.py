# Controlling LED (Digital Output):

import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM numbering)
GPIO.setmode(GPIO.BCM)

# Define pin for LED output
led_pin = 17

# Set pin as output
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn LED on
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)  # Delay 1 second
        
        # Turn LED off
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)  # Delay 1 second

finally:
    GPIO.cleanup()  # Clean up GPIO on program exit
