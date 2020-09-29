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
            robot.straight(365)
            robot.turn(45)
            print("Den turner anden gang")
            Kør_Lige_ud(robot,sensor,threshold,-4)



def FireGrå(robot, sensor, grey, white,ev3):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-45)
    print("TURNER 1. GANG")
    robot.straight(290)

    while (sensor.reflection() > grey):
        robot.drive(150,0)
        print("SER HVID, ALT ER GODT")
    robot.stop()
    robot.turn(30)
    print("TURNER 2. GANG")
    Kør_Lige_ud(robot,sensor,threshold,-4)




