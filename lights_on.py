import definitions
import RPi.GPIO as GPIO
import signal
import sys

lightpin = definitions.channel1pin
run = True

def handler_stop_signals(signum, frame):
    global run
    run = False

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
lightpin = 17
GPIO.setup(lightpin, GPIO.OUT)

while run:
    GPIO.output(17, GPIO.HIGH)


GPIO.cleanup()
sys.exit()