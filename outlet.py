!#/usr/bin/python3
import device
import abc
import lights_on
import subprocess


@device.register
class outlet(abc.ABC):
    @abc.abstractmethod
    def On(self):
        subprocess.Popen(['python', '/home/pi/weedbox/lights_on.py'])
    @abc.abstractmethod
    def Off(self):
        subprocess.Popen(['python', '/home/pi/weedbox/lights_off.py'])
    @abc.abstractmethod
    def State(self):
        pass