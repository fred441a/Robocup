#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor,  UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Direction

#Vores Libraries
from Ligeud import Kør_Lige_ud

# Initialize the motors.
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=[12,20])
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=[12,20])
Arm_Motor = Motor(Port.D)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)

#intialize the ultrasonic sensor
ultra_sensor =  UltrasonicSensor(Port.S2)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=191)

#Initialize the ev3 block
ev3 = EV3Brick()

# follow line until black cross line (use def kør_lige_ud)
while True:
    if Button.DOWN in ev3.buttons.pressed():
        BLACK = line_sensor.reflection()
        ev3.speaker.beep()
    if Button.UP in ev3.buttons.pressed():
        WHITE = line_sensor.reflection()
        ev3.speaker.beep()
    if BLACK != None and WHITE != None:
        threshold = (BLACK + WHITE) / 2
        Kør_Lige_ud(robot,line_sensor,threshold,-2)

# first turn
def indtil_hurdle():
    DriveBase.straight(50)
    DriveBase.turn(-45)
    DriveBase.stop()

# drive until wall detected
def første_væg():
    while True:
        # Begin driving forward at 100 millimeters per second.
        robot.reset_angle(0)
        robot.drive(100, 0)
        # Wait until an obstacle is detected. This is done by repeatedly
        # doing nothing (waiting for 5 milliseconds) while the measured
        # distance is still greater than 300 mm.
        while ultra_sensor.distance() > 40:
            wait(5)
        længde = robot.angle()
        # Turn right by 90 degrees
        robot.turn(90)

def væk_igen():
    while True:
        # Begin driving forward at 100 millimeters per second.
        robot.reset_angle(0)
        robot.drive(100, 0)
        # Wait until an obstacle is detected. This is done by repeatedly
        # doing nothing (waiting for 5 milliseconds) while the measured
        # distance is still greater than 300 mm.
        while robot.angle() > længde:
            wait(5)
        # Turn right by 90 degrees
        robot.turn(-45)

def ret_ind():
    while True:
        robot.drive(200,0)
        Kør_Lige_ud(robot,line_sensor,threshold,-2)
