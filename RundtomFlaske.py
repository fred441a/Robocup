from Ligeud import Kør_Lige_ud

def Rundt_Om_Flaske(robot,sensor,grey):
    robot.turn(45)
    robot.straight(600)
    robot.turn(-80)
    robot.straight(350)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        robot.drive(200,0)
    robot.stop()
    robot.turn(55)

def Rundt_Om_Flaske2(robot,sensor,grey):
    robot.turn(-45)
    robot.straight(600)
    robot.turn(80)
    robot.straight(250)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        robot.drive(200,0)
    robot.stop()
    robot.turn(-60)

def SjetteSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske(robot,line_sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,-4)

def OttendeSegment(robot,line_sensor,threshold,BLACK):
    Rundt_Om_Flaske2(robot,line_sensor,BLACK)
    Kør_Lige_ud(robot,line_sensor,threshold,4)