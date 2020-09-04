#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
Wheel_motors = Motor(Port.B,Port.C)
color_sensor = ColorSensor(Port.S3)

# Write your program here.
ev3.speaker.beep()
Motors.runtime(180,3000,then=Stop,wait=True)
m.run_forever(speed_sp=900)
m.stop(stop_action="hold")
#This is a test from your fellow Student FRED

# Connect an EV3 color sensor to any sensor port.
cl = ColorSensor()