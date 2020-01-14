
import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
lightpin = 17
GPIO.setup(lightpin, GPIO.OUT)

GPIO.output(17, GPIO.LOW)


GPIO.cleanup()
sys.exit()