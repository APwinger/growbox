# growbox
# growbox
Growbox is a raspberry pi controlled indoor grow-tent for growing "tomato-like" plants. 

Growbox works via crontab, the master.py script should be set to run every minute or every hour

The electronic control comes from a ADJ SRP8 power pack relay. This is connected, via a dsub 9 pin connector to the pi's gpio. 

the master.py script will start a subprocess script, lights.py between the hours of midnight and 7pm. Between 7pm and midnight of the next day, lights.py will be killed and light_off.py will be called for redundancy.

master.py spawns another subprocess, watering.py which triggers an x gph water pump on 



The script updates humidity.csv in the web/ folder with relative humidity and temperature values pulled from a DHT11 sensor as well as if the lights on are or off. 

