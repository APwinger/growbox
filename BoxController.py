#!/usr/bin/python3
from Outlet import Outlet
from Sensor import Sensor
import definitions

light = Outlet(1)
humidifier = Outlet(2)
pump = Outlet(3)
tNh = Sensor(4)

def lightsTwentyOn():
    if definitions.h < 20:
        light.on()   
    else:
        light.off()

#humidifier will maintain VPD according to sensor readings
def humidify(sensor):
    if not isinstance(sensor, Sensor):
        raise ValueError("sensor must be a Sensor")
    values = sensor.read()
    temp = values['temp']
    hum = values['hum']
    if isinstance(hum, float):
        if(hum < 45):
            humidifier.on()
        

while True:
    lightsTwentyOn()
    values = tNh.read()
    print("temp: ", values['temp'], "hum:", values['hum'])



