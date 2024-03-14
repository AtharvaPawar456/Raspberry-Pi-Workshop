# PIR sensor 

import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM numbering)
GPIO.setmode(GPIO.BCM)

# Set pin connected to PIR sensor
pir_pin = 4

# Set pin as input
GPIO.setup(pir_pin, GPIO.IN)

try:
    print("PIR Motion Sensor Test (CTRL+C to exit)")
    time.sleep(2)  # Warm-up time for sensor

    while True:
        if GPIO.input(pir_pin):  # Check if motion detected
            print("Motion detected!")
        else:
            print("No motion detected")

        time.sleep(1)  # Check for motion every 1 second

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO on program exit
