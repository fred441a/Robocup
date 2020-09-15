from Ligeud import Kør_Lige_ud

def Rundt_Om_Flaske(DriveBase,sensor,grey):
    robot.turn(45)
    robot.straight(250)
    robot.turn(-45)
    robot.straight(250)
    print(grey)
    while line_sensor.reflection() > grey:
        print(line_sensor.reflection())
        robot.drive(100,0)
    robot.stop()
    robot.turn(45)

def SjetteSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,-2)

def OttendeSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,2)