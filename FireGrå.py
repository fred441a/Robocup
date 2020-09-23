from Ligeud import Kør_Lige_ud

def SerIkkeGrå1(robot, sensor, grey, white, ev3):
    print("SER GRÅ, LEDER EFTER HVID")
    threshold = (grey+white)/2
    ev3.speaker.beep()
    robot.turn(-10)

    if(sensor.reflection() > grey):
        robot.straight(190)
        print("HAR FUNDET HVID")

        if(sensor.reflection() > grey):
            robot.straight(175)
            robot.turn(45)
            print("Den turner anden gang")
            Kør_Lige_ud(robot,sensor,threshold,-3)

def SerIkkeGrå2(robot, sensor, grey, white, ev3):
    print("den ser grå2")
    threshold = (grey+white)/2
    ev3.speaker.beep()
    robot.turn(-10)

    if(sensor.reflection() > grey):
        robot.straight(175)
        robot.turn(45)
        print("Den turner anden gang")
        Kør_Lige_ud(robot,sensor,threshold,-3)




def FireGrå(robot, sensor, grey, white,ev3):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-45)
    print("TURNER 1. GANG")

    if(sensor.reflection() > grey):
        print("SER HVID, ALT ER GODT")
        robot.straight(190)
        

        if(sensor.reflection() > grey):
            print("SER HVID IGEN, ALT ER GODT")
            robot.straight(175)
            robot.turn(45)
            
            Kør_Lige_ud(robot,sensor,threshold,-3)

        else:
            SerIkkeGrå2(robot, sensor, grey, white, ev3)
            
    else:
            SerIkkeGrå1(robot, sensor, grey,white, ev3)
            



