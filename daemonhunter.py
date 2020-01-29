#!/usr/bin/python3
import subprocess
import psutil
import definitions
import sys


h = definitions.h
loc = definitions.location
script = 'switch.py'
#arg 1 = channel arg 2 = on (true) or off (false)
channel = sys.argv[1]
on = sys.argv[2]
found = False

print(channel, on)
for process in psutil.process_iter():
    if process.cmdline() == ['python', loc + script, channel]:
        #check to see if lights should be on or off
        if on:
            print('Process found. Not opening it.')
            found = True
            break
        if off:
            #kill the light
            print('Process found. Terminating it.')
            process.terminate()
            print("channel: " + channel + " off")
            found = True

if not found and on:
    print('Process not found, should be running, starting now...')
    subprocess.Popen(['python', loc + script, channel])
