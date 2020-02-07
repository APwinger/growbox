#!/usr/bin/python3
import subprocess
import psutil
import definitions
import sys
from debug import debug

# Using Daemonhunter.py:
#     daemonhunter(int channel, boolean on)
#     channel is an outlet number 1-8 (converted via definitions.pinMap to BCM spec)
#     on = True(on), False(off)

def daemonhunter(channel, on):
    if not isinstance(channel, int):
        raise ValueError("channel needs to be an int", channel)
    h = definitions.h
    loc = definitions.location
    script = 'switch.py'
    found = False

    debug('python' + str(loc + script) + str(channel))
    for process in psutil.process_iter():
        if process.cmdline() == ['python', str(loc + script), str(channel)]:
            #check to see if lights should be on or off
            if on:
                debug('Process found. Not opening it.')
                found = True
                break
            if not on:
                #kill the light
                debug('Process found. Terminating it.')
                process.terminate()
                debug("channel: " + str(channel) + " off")
                found = True

    if not found and on:
        debug('Process not found, should be running, starting now...')
        #print(loc + script, channel)
        subprocess.Popen(['python', loc + script, str(channel)])

