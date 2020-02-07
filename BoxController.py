#!/usr/bin/python3
from Outlet import Outlet
from Sensor import Sensor
import definitions
import psutil

for process in psutil.process_iter():
        if process.cmdline() == ['/home/pi/growbox/venv/bin/python', '/home/pi/growbox/BoxController.py']:
            exit()

light = Outlet(1)
humidifier = Outlet(2)
pump = Outlet(3)
tNh = Sensor(4)

def lightsTwentyOn():
    if definitions.h < 20:
        light.on()   
    else:
        light.off()

#humidifier will keep humidity above 45%
def humidify(sensor):
    if not isinstance(sensor, Sensor):
        raise ValueError("sensor must be a Sensor")
    values = sensor.read()
    temp = values['temp']
    hum = float(values['hum'])
    if(hum < definitions.desiredHum):
        humidifier.on()
    else:
        humidifier.off()
        

while True:
    lightsTwentyOn()
    humidify(tNh)
    #values = tNh.read()
    #print("temp: ", values['temp'], "hum:", values['hum'])



