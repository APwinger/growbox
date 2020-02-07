# growbox
# growbox
Growbox is a raspberry pi controlled indoor grow-tent for growing tomato-like plants. 

BoxController.py should always be running, it is the main daemon script that will spawn every thing else. 

There are two classes in this project, Sensors and Outlets. 

Sensors will return a value, Outlets can be switched on and off. 

Switching in this project is weird:
    Currently using RPi GPIO for controlling a 120v relay (ADJ SRP8)
    In order to keep something on, I need to pull a pin high for however long.
    This is done by spawning the switch script, using daemonhunter.py. 

#Electronics
    ADJ SRP8 Power pack relay - 120v relay
    MIC2981 - transistor to switch 12v control circuits for relay 
    RPi 3 - using 3.3v gpio to switch transistor channels