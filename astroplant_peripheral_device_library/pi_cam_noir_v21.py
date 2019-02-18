"""
Implementation for the Pi Camera Noir V2.1
Should be similar for other camera's connected to the CSI interface on the Raspberry Pi
"""

import time

import asyncio
import pigpio
from astroplant_kit.peripheral import *

def growth_light_control_dummy(desired_state):
    pass

class PI_CAM_NOIR_V21(Camera):

    VIS_CAPABLE = True
    NIR_CAPABLE = True

    def __init__(self, *args, pi, light_pins, growth_light_control, **kwargs):
        super().__init__(*args, pi, light_pins, growth_light_control, **kwargs)

    async def make_photo_vis(self, command):
        if command == CameraCommandType.REGULAR_PHOTO:
            return make_regular_photo()
        else:
            return leaf_mask()

    async def make_regular_photo(self):
        #self.growth_light_control(GROWTH_LIGHT_CONTROL.OFF)

        #self.light_pins["white"]
        pass

    async def leaf_mask(self):
        pass

    def sanity_check(self):
        if VIS_CAPABLE == True:
            try:
                print("White light pin: {}".format(self.light_pins["white"]))
            except KeyError:
                print("ERROR, no white light pin defined in dict light_pins...")

            try:
                print("Red light pin: {}".format(self.light_pins["red"]))
            except KeyError:
                print("ERROR, no red light pin defined in dict light_pins...")

            try:
                print("Green light pin: {}".format(self.light_pins["red"]))
            except KeyError:
                print("ERROR, no green light pin defined in dict light_pins...")
