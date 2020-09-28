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



def FireGrå(drivebase,ultra_sensor,line_sensor,BLACK, WHITE):
    robot.straight(500)
    robot.turn(-45)
    robot.straight(400)
    print("TURNER 1. GANG")
    robot.turn(30)
    Kør_Lige_ud(robot,sensor,threshold,-2)
        
            




