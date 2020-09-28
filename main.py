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
from vippe import TredjeSegment, TredjeSegment_alt
from HenteFlaske import AndetSegment , løfte_flaske
from Målskive import FemteSegment



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

        
def FinalFunction(robot,line_sensor,threshold,BLACK,WHITE,ultra_sensor):
        FørsteSegment(robot,line_sensor,threshold,BLACK)
        Kør_Lige_ud(robot,line_sensor,threshold,-4)
        ev3.speaker.say("Done with first segment")
        AndetSegment(robot,Arm_Motor,ultra_sensor,line_sensor,threshold)
        ev3.speaker.say("Done with second segment")
        TredjeSegment_alt(robot,line_sensor,threshold,BLACK,WHITE)
        FireGrå(robot,line_sensor,BLACK,WHITE,ev3)
        ev3.speaker.say("Done with four grey")
        FemteSegment(robot,line_sensor,ultra_sensor, threshold,BLACK,Arm_Motor, ev3)
        SjetteSegment(robot,line_sensor,threshold,BLACK)
        ev3.speaker.say("done with six segment")
        SyvendeSegment(robot,ultra_sensor)
        Kør_Lige_ud(robot,line_sensor,threshold,-2)
        ev3.speaker.say("done with seventh segment")
        OttendeSegment(robot,line_sensor,threshold,BLACK)
        ev3.speaker.say("done with eight segment")
        stop_på_midten(robot, ultra_sensor)


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
        FinalFunction(robot,line_sensor,threshold,BLACK,WHITE,ultra_sensor)
        #AndetSegment(robot,Arm_Motor,ultra_sensor,line_sensor,threshold)
        #TredjeSegment(robot,line_sensor,threshold)
        stop_på_midten(robot, line_sensor, ultra_sensor, threshold)
        break
