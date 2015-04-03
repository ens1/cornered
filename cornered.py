#!/usr/bin/env python2
#Reads cursor location and creats hot corners


import time, ConfigParser, os
from Xlib import display, X
from subprocess import Popen




d=display.Display()
width_in_pixels=d.screen().width_in_pixels
height_in_pixels=d.screen().height_in_pixels

config=ConfigParser.ConfigParser()
config.read(os.path.expanduser("~/.corneredconf"))

top_left_command=""
bottom_left_command=""
top_right_command=""
bottom_right_command=""



try:
    top_left_command=config.get("config", "top_left")
    bottom_left_command=config.get("config", "bottom_left")
    top_right_command=config.get("config", "top_right")
    bottom_right_command=config.get("config", "bottom_right")
except ConfigParser.NoSectionError:
    print "Config file incorrect or missing from ~/.corneredconf"
    exit()
except ConfigParser.NoOptionError:
    pass

def exec_command(command):
    try:
        Popen(command)
    except OSError:
        pass

while True:
    x_coord=d.screen().root.query_pointer().win_x
    y_coord=d.screen().root.query_pointer().win_y
    
    if x_coord < 3:
        if y_coord < 3:
            exec_command(top_left_command.split(' '))
            time.sleep(.6)

        if y_coord > height_in_pixels - 3:
            exec_command(bottom_left_command.split(' '))
            time.sleep(.6)

    if x_coord > width_in_pixels - 3:
        if y_coord < 3:
            exec_command(top_right_command.split(' '))
            time.sleep(.6)

        if y_coord > height_in_pixels - 3:
            exec_command(bottom_right_command.split(' '))
            time.sleep(.6)

    time.sleep(.08)
