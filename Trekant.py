from pybricks.tools import wait
from Ligeud import Kør_Lige_ud_Ind_TIL_Langsomt

# first turn
def indtil_hurdle(DriveBase):
    DriveBase.straight(700)
    DriveBase.turn(-45)
    DriveBase.stop()

# drive until wall detected
def første_væg(robot,ultra_sensor):
    # Begin driving forward at 100 millimeters per second.
    robot.reset()
    robot.drive(100, 0)
    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 5 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while ultra_sensor.distance() > 160:
        wait(5)
    længde = robot.distance()
    print(robot.distance())
    # Turn right by 90 degrees
    robot.turn(90)
    væk_igen(robot,længde)

def væk_igen(robot,længde):
    # Begin driving forward at 100 millimeters per second.
    robot.reset()
    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 5 milliseconds) while the measured
    # distance is still greater than 300 mm.
    robot.straight(længde+30)
    # Turn right by 90 degrees
    robot.turn(-45)

def ret_ind(robot):
    robot.straight(400)
        
def SyvendeSegment(robot, ultra_sensor,line_sensor,threshold):
    Kør_Lige_ud_Ind_TIL_Langsomt(robot,line_sensor,threshold, -1,2000)
    indtil_hurdle(robot)
    første_væg(robot,ultra_sensor)
    ret_ind(robot)
