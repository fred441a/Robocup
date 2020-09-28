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
from vippe import TredjeSegment_alt
from HenteFlaske import AndetSegment , løfte_flaske
from Målskive import FemteSegment

Arm_Motor = Motor(Port.D)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=191)

#Initialize the ev3 block
ev3 = EV3Brick()

Arm_Motor.run_target(300,-1500)