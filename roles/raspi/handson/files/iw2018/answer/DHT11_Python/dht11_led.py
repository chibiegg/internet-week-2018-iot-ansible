import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 22
instance = dht11.DHT11(pin=22)

# LED setup
LED = 36
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            GPIO.output(LED, GPIO.HIGH)

        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)

finally:
    GPIO.cleanup()
