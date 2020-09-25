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
    robot.straight(340)

    while (sensor.reflection() > grey):
        robot.drive(150,0)
        print("SER HVID, ALT ER GODT")

    robot.turn(30)
    print("TURNER 2. GANG")
    Kør_Lige_ud(robot,sensor,threshold,-4)
        
     
    else:
            SerIkkeGrå1(robot, sensor, grey,white, ev3)
            
def FireGråAlternativ(robot, sensor, grey, white,ev3):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-45)
    print("TURNER 1. GANG")
    robot.straight(200)

    while sensor.reflection() > grey:
        print("SER HVID, ALT ER GODT")
        robot.drive(150,0)
        
        if sensor.reflection() < white:
            print("SER GRÅ")
            robot.stop()
            robot.turn(45)
            Kør_Lige_ud(robot,sensor,threshold,-4)
            
            if sensor.reflection < grey:
                robot.stop()
                break
            wait(10)



