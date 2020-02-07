#!/usr/bin/python3
import subprocess
from daemonhunter import daemonhunter

class Outlet:
    def __init__(self, number):
        self.number = number

    def on(self):
        daemonhunter(self.number, True)
    def off(self):
        daemonhunter(self.number, False)
    def state(self):
        pass