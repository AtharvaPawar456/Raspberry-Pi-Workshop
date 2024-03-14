# Mall Door Opening System


# pip install gpiozero

import RPi.GPIO as GPIO
import time
from gpiozero import Servo

# Set GPIO mode (BCM numbering)
GPIO.setmode(GPIO.BCM)

# Set pin connected to PIR sensor
pir_pin = 4

# Set pin connected to servo
servo_pin = 17

# Set pin as input
GPIO.setup(pir_pin, GPIO.IN)

def set_servo_angle(angle):
    # Create a Servo object
    servo = Servo(servo_pin)

    try:
        # Convert angle to a value between -1 (0 degrees) and 1 (180 degrees)
        angle_value = (angle / 180.0) * 2 - 1

        # Set the servo to the specified angle
        servo.value = angle_value
        time.sleep(1)  # Adjust delay as needed for your servo to reach the position

    finally:
        servo.close()  # Clean up servo resources

try:
    print("PIR Motion Sensor Test (CTRL+C to exit)")
    time.sleep(2)  # Warm-up time for sensor

    while True:
        if GPIO.input(pir_pin):  # Check if motion detected
            print("Motion detected!")
            set_servo_angle(0)  # Rotate servo to 0 degrees
            time.sleep(20)  # Delay for 20 seconds
            set_servo_angle(180)  # Rotate servo to 180 degrees
            time.sleep(20)  # Delay for 20 seconds
        else:
            print("No motion detected")

        time.sleep(1)  # Check for motion every 1 second

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO on program exit
