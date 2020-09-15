from Ligeud import Kør_Lige_ud

def Rundt_Om_Flaske(DriveBase,sensor,grey):
    DriveBase.turn(45)
    DriveBase.straight(250)
    DriveBase.turn(-45)
    DriveBase.straight(250)
    print(grey)
    while line_sensor.reflection() > grey:
        print(line_sensor.reflection())
        DriveBase.drive(100,0)
    DriveBase.stop()
    DriveBase.turn(45)

def SjetteSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(DriveBase,sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,-2)

def OttendeSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(DriveBase,sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,2)