import time

#in the future these will query model to get values
channel1pin = 17
channel2pin = 27
location = '/home/pi/growbox/'
t = time.localtime() # gives you an actual struct_time object
h = t.tm_hour
#set true to enable debugging outputs
debug = False

#outlet numbers (ADJ SRP8, 1-8) to BCM pins on RPi 3
pinMap = { 1:17, 2:23, 3:22, 4:27}