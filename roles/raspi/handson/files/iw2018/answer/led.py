# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PIN = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN, GPIO.HIGH)

time.sleep(1)
GPIO.cleanup()


