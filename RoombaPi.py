# Imports
import webiopi
import pyrobot
import time


# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #

# Left motor GPIOs
#L1=9  # H-Bridge 1
#L2=10 # H-Bridge 2
#LS=11 # H-Bridge 1,2EN

# Right motor GPIOs
#R1=23 # H-Bridge 3
#R2=24 # H-Bridge 4
#RS=25 # H-Bridge 3,4EN

# -------------------------------------------------- #
# Convenient PWM Function                            #
# -------------------------------------------------- #

# Set the speed of two motors
#def set_speed(speed):
#    GPIO.pulseRatio(LS, speed)
#    GPIO.pulseRatio(RS, speed)

# -------------------------------------------------- #
# Left Motor Functions                               #
# -------------------------------------------------- #

#def left_stop():
#    GPIO.output(L1, GPIO.LOW)
#    GPIO.output(L2, GPIO.LOW)

#def left_forward():
#    GPIO.output(L1, GPIO.HIGH)
#    GPIO.output(L2, GPIO.LOW)

#def left_backward():
#    GPIO.output(L1, GPIO.LOW)
#    GPIO.output(L2, GPIO.HIGH)

# -------------------------------------------------- #
# Right Motor Functions                              #
# -------------------------------------------------- #
#def right_stop():
#    GPIO.output(R1, GPIO.LOW)
#    GPIO.output(R2, GPIO.LOW)

#def right_forward():
#    GPIO.output(R1, GPIO.HIGH)
#    GPIO.output(R2, GPIO.LOW)

#def right_backward():
#    GPIO.output(R1, GPIO.LOW)
#    GPIO.output(R2, GPIO.HIGH)

# -------------------------------------------------- #
# Macro definition part                              #
# -------------------------------------------------- #

def led_on():
    GPIO.output(24, GPIO.HIGH)

def led_off():
    GPIO.output(24, GPIO.LOW)

def go_forward():
    r.DriveStraight(pyrobot.VELOCITY_FAST)
    #left_forward()
    #right_forward()

def go_backward():
    r.DriveStraight(-pyrobot.VELOCITY_FAST)
    #left_backward()
    #right_backward()

def turn_left():
    r.TurnInPlace(pyrobot.VELOCITY_SLOW, 'ccw')
    #left_backward()
    #right_forward()

def turn_right():
    r.TurnInPlace(pyrobot.VELOCITY_SLOW, 'cw')
    #left_forward()
    #right_backward()

def stop():
    r.Stop()
    #left_stop()
    #right_stop()
    
#  loop which toggles LED attached to GPIO 24 every 5 seconds
def loop():
    GPIO.output(24, not GPIO.input(24))
    time.sleep(5)        

def MacroWithArgs(arg1, arg2):
    r.sensors.GetAll()
    voltage = r.sensors['voltage']/1000.00
    capacity = r.sensors['capacity']
    charge = r.sensors['charge']
    return("%s %s %s" % (voltage, capacity, charge))


# -------------------------------------------------- #
# Initialization part                                #
# -------------------------------------------------- #

# Setup GPIOs
#GPIO.setFunction(LS, GPIO.PWM)
#GPIO.setFunction(L1, GPIO.OUT)
#GPIO.setFunction(L2, GPIO.OUT)

#GPIO.setFunction(RS, GPIO.PWM)
#GPIO.setFunction(R1, GPIO.OUT)
GPIO.setFunction(24, GPIO.OUT)

#set_speed(0.5)
#stop()

# Init serial 
r = pyrobot.Roomba(tty = '/dev/ttyAMA0')
#r.sci.Wake()
r.Control()

# Do a little POST dance
r.TurnInPlace(pyrobot.VELOCITY_SLOW, 'cw')
time.sleep(0.5)
r.TurnInPlace(pyrobot.VELOCITY_SLOW, 'ccw')
time.sleep(0.5)
r.DriveStraight(pyrobot.VELOCITY_SLOW)
time.sleep(0.25)
r.DriveStraight(-pyrobot.VELOCITY_SLOW)
time.sleep(.25)
r.Stop()

stop()

# -------------------------------------------------- #
# Main server part                                   #
# -------------------------------------------------- #

# Instantiate the server on the port 8000, it starts immediately in its own thread
server = webiopi.Server(port=8000, login="roomba", password="pi")

# Register the macros so you can call it with Javascript and/or REST API

server.addMacro(go_forward)
server.addMacro(go_backward)
server.addMacro(turn_left)
server.addMacro(turn_right)
server.addMacro(stop)
server.addMacro(led_on)
server.addMacro(led_off)
server.addMacro(MacroWithArgs)

# -------------------------------------------------- #
# Loop execution part                                #
# -------------------------------------------------- #

# Run our loop until CTRL-C is pressed or SIGTERM received
webiopi.runLoop(loop)

# If no specific loop is needed and defined above, just use 
# webiopi.runLoop()


# -------------------------------------------------- #
# Termination part                                   #
# -------------------------------------------------- #

# Stop the server
server.stop()

# Reset GPIO functions
#GPIO.setFunction(LS, GPIO.IN)
#GPIO.setFunction(L1, GPIO.IN)
#GPIO.setFunction(L2, GPIO.IN)

#GPIO.setFunction(RS, GPIO.IN)
#GPIO.setFunction(R1, GPIO.IN)
#GPIO.setFunction(R2, GPIO.IN)

