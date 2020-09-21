from Ligeud import Kør_Lige_ud

def Rundt_Om_Flaske(robot,sensor,grey):
    robot.turn(45)
    robot.straight(250)
    robot.turn(-45)
    robot.straight(250)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        robot.drive(100,0)
    robot.stop()
    robot.turn(45)

def SjetteSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,line_sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,-2)

def OttendeSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,line_sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,2)