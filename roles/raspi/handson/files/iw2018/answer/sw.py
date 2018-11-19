# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

LED = 22
SW = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		GPIO.output(LED, GPIO.LOW)
		input = GPIO.input(SW)
		if input == GPIO.LOW:
			print("pressed")
			time.sleep(1)
			GPIO.output(LED, GPIO.HIGH)
			time.sleep(1)

finally:
	GPIO.cleanup()

