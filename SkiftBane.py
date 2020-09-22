from Ligeud import Kør_Lige_ud , Kør_Lige_ud_Ind_TIL
from pybricks.tools import wait

def Skift_linje_Højre(DriveBase,sensor,grey):
    DriveBase.turn(45)
    DriveBase.straight(50)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        DriveBase.drive(200,0)
    DriveBase.stop()
    DriveBase.turn(-45)

def Skift_linje_Venstre(DriveBase,sensor,grey):
    DriveBase.turn(-45)
    DriveBase.straight(50)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        DriveBase.drive(200,0)
    DriveBase.stop()
    DriveBase.turn(45)

def FørsteSegment(robot,line_sensor,threshold,BLACK):
        Kør_Lige_ud(robot,line_sensor,threshold,-2)
        Skift_linje_Højre(robot,line_sensor,BLACK)
        Kør_Lige_ud(robot,line_sensor,threshold,2)
        Skift_linje_Venstre(robot,line_sensor,BLACK)
        Kør_Lige_ud_Ind_TIL(robot,line_sensor,threshold,-3, 10)
        Kør_Lige_ud(robot,line_sensor,threshold,3)
        