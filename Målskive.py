from Ligeud import Kør_Lige_ud
from HenteFlaske import løfte_flaske

def FemteSegment(drivebase,line_sensor,ultra_sensor, threshold,grå,Arm_motor, ev3):
    drivebase.straight(200)
    drivebase.turn(-90)
    drivebase.reset()
    Kør_Lige_ud(drivebase,line_sensor,threshold,-2)
    drivebase.straight(600)
    løfte_flaske(Arm_motor,False)
    drivebase.straight(-drivebase.distance())
    drivebase.turn(90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,2)


def tæl_streger(line_sensor,drivebase,grå,Arm_motor,ev3):
    Streger = 0
    while True:
        drivebase.drive(100,0)
        if line_sensor.reflection() <= grå:
            Streger = Streger+1
            ev3.speaker.beep()
        if Streger == 3:
            løfte_flaske(Arm_motor,False)


