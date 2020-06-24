#!/usr/bin/env python3
import signal
from fanshim import FanShim
import os

"""
This script allows the pimoroni-fanshim.service to be started and stopped using
FanSHIM's button.
"""

fanshim = FanShim()

# Set the button hold time, in seconds
fanshim.set_hold_time(1.0)

#The loop checks constantly whether the button is pressed, held or not
while True:
    @fanshim.on_press()
    #when the button is pressed, the pimoroni-fanshim.service is stopped
    def press():
        os.system('sudo systemctl stop pimoroni-fanshim.service')
        

    #when the button is held, the pimoroni-fanshim.service is started
    @fanshim.on_hold()
    def hold():
        os.system('sudo systemctl start pimoroni-fanshim.service')


