#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.ev3devices import Motor, ColorSensor,  UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Direction
from Ligeud import Kør_Lige_ud
from SkiftBane import Skift_linje_Højre , Skift_linje_Venstre
from HenteFlaske import dreje_mod_flaske

# Initialize the motors.
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
Arm_Motor = Motor(Port.D)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)

#intialize the ultrasonic sensor
ultra_sensor =  UltrasonicSensor(Port.S2)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=191)

#Initialize the ev3 block
ev3 = EV3Brick()

# Calculate the light threshold. Choose values based on your measurements.


BLACK = None
WHITE = None



# Start following the line endlessly.

while True:
        Kør_hen_til_flaske(robot,ultra_sensor)
        løfte_flaske(robot,ultra_sensor)
        
        break