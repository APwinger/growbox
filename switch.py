import definitions
import RPi.GPIO as GPIO
import signal
import sys
from debug import debug


pin = definitions.pinMap[int(sys.argv[1])]
debug(pin + " turning on")
run = True

def handler_stop_signals(signum, frame):
    global run
    run = False

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while run:
    GPIO.output(pin, GPIO.HIGH)


GPIO.cleanup()
sys.exit()