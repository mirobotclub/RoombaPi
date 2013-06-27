#!/usr/bin/python

# The MIT License
#
# Copyright (c) 2013 James Ronald
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import pyrobot
import time
import signal
import sys

def signal_handler(signal, frame):
        print('Stopping!! - You pressed Ctrl-C')
	r.Stop()
        sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)

  """Do a little dance."""
  r = pyrobot.Roomba(tty = '/dev/ttyAMA0')
  r.sci.Wake()
  r.safe=False
  r.Control()
  r.TurnInPlace(pyrobot.VELOCITY_SLOW, 'cw')
  time.sleep(0.5)
  r.TurnInPlace(pyrobot.VELOCITY_SLOW, 'ccw')
  time.sleep(0.5)
  r.DriveStraight(pyrobot.VELOCITY_SLOW)
  time.sleep(0.25)
  r.DriveStraight(-pyrobot.VELOCITY_SLOW)
  time.sleep(.25)
  r.Stop()


  voltage_prev = 0 

  while True:

    r.sensors.GetAll()           

    if r.sensors['bump-left']:
        r.Drive(-pyrobot.VELOCITY_SLOW, 10)
        time.sleep(.25)
    elif r.sensors['bump-right']:
        r.Drive(pyrobot.VELOCITY_SLOW, 10)
        time.sleep(.25)
    else:
        r.DriveStraight(pyrobot.VELOCITY_SLOW)
        time.sleep(.25)

    voltage = r.sensors['voltage']/1000.00
    if voltage_prev != voltage:
       print(voltage)
       voltage_prev = voltage
