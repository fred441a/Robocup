#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor,  UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Direction

#Vores Libraries
from Ligeud import Kør_Lige_ud
from SkiftBane import FørsteSegment
from Trekant import SyvendeSegment
from RundtomFlaske import Rundt_Om_Flaske, SjetteSegment, OttendeSegment
from Stoppåmidten import stop_på_midten
from FireGrå import FireGrå



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

# Calculate the light threshold. Choose values based on your measurements.


BLACK = None
WHITE = None

#Løser det første segment hvor robotten skal skifte linje 2 gange



# Start following the line endlessly.

while True:
    if Button.DOWN in ev3.buttons.pressed():
        BLACK = line_sensor.reflection()
        ev3.speaker.beep()
    if Button.UP in ev3.buttons.pressed():
        WHITE = line_sensor.reflection()
        ev3.speaker.beep()
    if BLACK != None and WHITE != None:
        threshold = (BLACK + WHITE) / 2
        
        FireGrå(robot,line_sensor,BLACK,WHITE,ev3)
        
        break
