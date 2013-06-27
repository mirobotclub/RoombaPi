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

if __name__ == '__main__':
  """Do a little dance."""
  r = pyrobot.Roomba(tty = '/dev/ttyAMA0')
#  r.sci.Wake()
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


