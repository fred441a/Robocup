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

        
def beeper(ev3,times):
    integer = times
    while integer > 0:
        ev3.speaker.beep()
        integer = 1-integer
        wait(10)

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
        FørsteSegment(robot,line_sensor,threshold,BLACK)
        ev3.speaker.beep()
        print("Færdig med første segment")
        Kør_Lige_ud(robot,line_sensor,threshold,2)
        beeper(ev3,2)
        Kør_Lige_ud(robot,line_sensor,threshold,2)
        beeper(ev3,3)
        FireGrå(robot,line_sensor,BLACK,WHITE)
        beeper(ev3,4)
        print("Færdig med fire grå")
        Kør_Lige_ud(robot,line_sensor,threshold,2)
        beeper(ev3,5)
        SjetteSegment(robot,line_sensor,threshold,BLACK)
        beeper(ev3,6)
        print("Færdig med sjette segment")
        SyvendeSegment(robot,ultra_sensor)
        beeper(ev3,7)
        Kør_Lige_ud(robot,line_sensor,threshold,2)
        beeper(ev3,8)
        print("Færdig med syvende segment")
        OttendeSegment(robot,line_sensor,threshold,BLACK)
        beeper(ev3,9)
        print("ottende segment")
        break
