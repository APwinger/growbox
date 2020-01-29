import time

lightPin = 17
aeratePin = 27
location = '/home/pi/growbox/'
t = time.localtime() # gives you an actual struct_time object
h = t.tm_hour