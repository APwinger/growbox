
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
waterpin = 27
GPIO.setup(waterpin, GPIO.OUT)
GPIO.output(waterpin, GPIO.HIGH)

time.sleep(15)

GPIO.output(waterpin, GPIO.LOW)

GPIO.cleanup()
