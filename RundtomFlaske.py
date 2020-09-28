from Ligeud import Kør_Lige_ud

def Rundt_Om_Flaske(robot,sensor,grey):
    robot.turn(45)
    robot.straight(600)
    robot.turn(-90)
    robot.straight(400)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        robot.drive(200,0)
    robot.stop()
    robot.turn(60)

def SjetteSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,line_sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,-3)

def OttendeSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,line_sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,3)