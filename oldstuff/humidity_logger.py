import os
import time
import Adafruit_DHT
import RPi.GPIO as GPIO


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


lightpin = 17
light =  "ERROR"

GPIO.setup(lightpin, GPIO.OUT)

f = open('/home/pi/weedbox/humidity.csv', 'a+')
if os.stat('/home/pi/weedbox/humidity.csv').st_size == 0:
   f.write('Date,Time,Temperature,Humidity,Light\r\n')

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if GPIO.input(lightpin) == GPIO.LOW:
	light = "OFF"
if GPIO.input(lightpin) == GPIO.HIGH:
	light = "ON"

if humidity is not None and temperature is not None:
    print('{0},{1},{2:0.1f}*C,{3:0.1f}%,{4}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, light))
    f.write('{0},{1},{2:0.1f},{3:0.1f},{4}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, light))
else:
    print("Failed to retrieve data from humidity sensor")


