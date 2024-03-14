# DHT11

# pip install Adafruit_DHT

import RPi.GPIO as GPIO
import Adafruit_DHT
import time

# Set DHT sensor type (DHT11)
sensor = Adafruit_DHT.DHT11

# Set GPIO pin connected to the sensor
pin = 4  # Example GPIO pin 4 (you can use any GPIO pin)

try:
    while True:
        # Attempt to get sensor readings
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Check if readings are valid
        if humidity is not None and temperature is not None:
            # Print temperature and humidity
            print(f'Temperature: {temperature:.1f}°C | Humidity: {humidity:.1f}%')
        else:
            print('Failed to retrieve data from sensor. Check connection.')

        # Delay between readings
        time.sleep(2)

except KeyboardInterrupt:
    print('Exiting...')
finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
