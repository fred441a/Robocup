from Ligeud import Kør_Lige_ud

#def SerIkkeGrå1(robot, sensor, grey, white, ev3):
    #print("SER GRÅ, LEDER EFTER HVID")
    #threshold = (grey+white)/2
    #ev3.speaker.beep()
    #robot.turn(-10)

    #if(sensor.reflection() > grey):
        #robot.straight(150)
        #print("HAR FUNDET HVID")

        #if(sensor.reflection() > grey):
            #robot.straight(365)
            #robot.turn(45)
            #print("Den turner anden gang")
            #Kør_Lige_ud(robot,sensor,threshold,-2)



def FireGrå(robot, sensor, grey, white,ev3):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-45)
    robot.straight(300)
    print("TURNER 1. GANG")
    robot.turn(30)

    while sensor.reflection() > grey:
        print(sensor.reflection())
        drivebase.drive(200,0)
        print("SER HVID, ALT ER GODT")
    Kør_Lige_ud(robot,sensor,threshold,-2)
        
            




