!#/usr/bin/python3
import subprocess
import psutil



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
