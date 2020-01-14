import os
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import subprocess
import signal
import psutil
import sys

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
lightpin = 17
light =  "ERROR"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(lightpin, GPIO.OUT)

#create/open hum/tem/light CSV
#perhaps move this to a DB
f = open('/home/pi/weedbox/web/humidity.csv', 'a+')
if os.stat('/home/pi/weedbox/web/humidity.csv').st_size == 0:
   f.write('Date,Time,Temperature,Humidity,Light\r\n')

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

t = time.localtime() # gives you an actual struct_time object
h = t.tm_hour


found = False

for process in psutil.process_iter():
    if process.cmdline() == ['python', '/home/pi/weedbox/lights_on.py']:
        #check to see if lights should be on or off
        if h < 20:
            print('Process found. Not opening it.')
            found = True
            break
        if h >= 20:
            #kill the light
            print('Process found. Terminating it.')
            process.terminate()
            subprocess.Popen(['python', '/home/pi/weedbox/lights_off.py'])
            print("light off")
            found = True

if not found and h < 20:
    print('Process not found, should be running, starting now...')
    subprocess.Popen(['python', '/home/pi/weedbox/lights_on.py'])

if GPIO.input(lightpin) == GPIO.LOW:
	light = "OFF"
if GPIO.input(lightpin) == GPIO.HIGH:
	light = "ON"

if humidity is not None and temperature is not None:
    print('{0},{1},{2:0.1f}*C,{3:0.1f}%,{4}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, light))
    f.write('{0},{1},{2:0.1f},{3:0.1f},{4}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, light))
else:
    print("Failed to retrieve data from humidity sensor")


sys.exit()
