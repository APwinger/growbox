import os
import Adafruit_DHT
import signal
import time

#currently not abstract, this is a humidity/temp sensor (DHT11), code will be abstracted 
#when I find another sensor and see how it works. 
class Sensor:
    def __init__(self, number):
        self.number = number
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = number

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        if humidity is not None and temperature is not None:
            return {'temp':temperature, 'hum':'{0:0.1f}'.format(humidity)}
        else:
            print("Failed to retrieve data from humidity sensor")

    def log(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        #create/open hum/tem/light CSV
        #perhaps move this to a DB
        #f = open('/home/pi/weedbox/web/humidity.csv', 'a+')
        #if os.stat('/home/pi/weedbox/web/humidity.csv').st_size == 0:
        #    f.write('Date,Time,Temperature,Humidity,Light\r\n')
        #f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        print('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))


