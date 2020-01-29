#!/usr/bin/python3
import subprocess
import psutil
import definitions
import sys

h = definitions.h
loc = definitions.location
#this should be the only argument
script = sys.argv[1]
found = False


for process in psutil.process_iter():
    if process.cmdline() == ['python', loc + script]:
        #check to see if lights should be on or off
        if h < 20:
            print('Process found. Not opening it.')
            found = True
            break
        if h >= 20:
            #kill the light
            print('Process found. Terminating it.')
            process.terminate()
            subprocess.Popen(['python', loc + script])
            print("light off")
            found = True

if not found and h < 20:
    print('Process not found, should be running, starting now...')
    subprocess.Popen(['python', loc + script])
