
#you need to use cron to run this every 12 hours
#another script should check to see if it is running in case it crashes??
#what about on reboot?
#can another script check the gpio?
import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

lightpin = 17
t = time.localtime() # gives you an actual struct_time object
h = t.tm_hour

GPIO.setmode(GPIO.BCM)
GPIO.setup(lightpin, GPIO.OUT)

while h < 20:
	GPIO.output(lightpin, GPIO.HIGH)

GPIO.output(17, GPIO.LOW)
GPIO.cleanup()
