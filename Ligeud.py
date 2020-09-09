from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

def Kør_Lige_ud(drivebase,linesensor,threshold):
        # Set the drive speed at 100 millimeters per second.
    DRIVE_SPEED = 100

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = 2
    while True:
        # Calculate the deviation from the threshold.
        deviation = linesensor.reflection() - threshold

        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        drivebase.drive(DRIVE_SPEED, turn_rate)

        # You can wait for a short time or do other things in this loop.
        if linesensor.reflection() < 15:
            print("STOP")
            break
        wait(10)

def Drej_tilhøjre():
DriveBase.turn(45)
DriveBase.straight(distance(200))