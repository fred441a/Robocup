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
<<<<<<< HEAD
from PickupFlask import PickupFlask , PutDownFlask
from FireGrå import FireGrå

=======
from HenteFlaske import dreje_mod_flaske
>>>>>>> 77cbc2b83ee94ac03ee7e7db6773477f6b1a7755

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
<<<<<<< HEAD
=======

>>>>>>> 77cbc2b83ee94ac03ee7e7db6773477f6b1a7755
while True:
    if Button.DOWN in ev3.buttons.pressed():
        BLACK = line_sensor.reflection()
        ev3.speaker.beep()
    if Button.UP in ev3.buttons.pressed():
        WHITE = line_sensor.reflection()
        ev3.speaker.beep()
<<<<<<< HEAD
    if Button.LEFT in ev3.buttons.pressed():
        if openclose:
            Arm_Motor.run(100)
            openclose = False
        else:
            Arm_Motor.run(-100)
            openclose = True
    if Button.RIGHT in ev3.buttons.pressed():
        Arm_Motor.stop()
    if BLACK != None and WHITE != None:
        threshold = (BLACK + WHITE) / 2
        FireGrå(robot,line_sensor,BLACK,WHITE)

        #Kør_Lige_ud(robot,line_sensor,threshold,-2)
        #Skift_linje_Højre(robot,line_sensor,BLACK)
        #Kør_Lige_ud(robot,line_sensor,threshold,2)
        #Skift_linje_Venstre(robot,line_sensor,BLACK)
        #Kør_Lige_ud(robot,line_sensor,threshold,-2)
=======
    if BLACK != None and WHITE != None:
        threshold = (BLACK + WHITE) / 2
        Kør_Lige_ud(robot,line_sensor,threshold,-2)
        Skift_linje_Højre(robot,line_sensor,BLACK)
        Kør_Lige_ud(robot,line_sensor,threshold,2)
        Skift_linje_Venstre(robot,line_sensor,BLACK)
        Kør_Lige_ud(robot,line_sensor,threshold,-2)
        dreje_mod_flaske(robot,line_sensor,BLACK)
        
>>>>>>> 77cbc2b83ee94ac03ee7e7db6773477f6b1a7755
        break
        


