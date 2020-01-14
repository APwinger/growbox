import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
lightpin = 17
GPIO.setup(lightpin, GPIO.OUT)
if GPIO.input(lightpin) == GPIO.LOW:
	if time.struct_time(tmtm_hour < 20:
		GPIO.output(17, GPIO.HIGH)
		time.sleep(68400)
GPIO.cleanup()

