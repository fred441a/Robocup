from pybricks.ev3devices import Motor, ColorSensor,  UltrasonicSensor
from pybricks.robotics import DriveBase

def stop_på_midten(DriveBase, ultra_sensor):
    while True:
        if ultra_sensor.distance() > 1368:
            DriveBase.drive(100,0)
        else:
            break