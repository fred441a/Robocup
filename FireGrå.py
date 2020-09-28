from Ligeud import Kør_Lige_ud

def SerIkkeGrå1(robot, sensor, grey, white, ev3):
    print("SER GRÅ, LEDER EFTER HVID")
    threshold = (grey+white)/2
    ev3.speaker.beep()
    robot.turn(-10)

    if(sensor.reflection() > grey):
        robot.straight(150)
        print("HAR FUNDET HVID")

        if(sensor.reflection() > grey):
            robot.straight(365)
            robot.turn(45)
            print("Den turner anden gang")
            Kør_Lige_ud(robot,sensor,threshold,-2)



def FireGrå(robot, sensor, grey, white,ev3):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-45)
    print("TURNER 1. GANG")

    while (sensor.reflection() > grey):
        robot.drive(100,0)
        print("SER HVID, ALT ER GODT")

    robot.turn(45)
    print("TURNER 2. GANG")
    Kør_Lige_ud(robot,sensor,threshold,-2)
        
            




