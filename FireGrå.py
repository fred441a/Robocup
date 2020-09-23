from Ligeud import Kør_Lige_ud

def FireGrå(robot, sensor, grey, white,ev3):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-45)
    print("Den turner første gang")

    if(sensor.reflection() >= grey):
        robot.straight(190)
        print("Den ser hvid og kører ligeud 17.5cm")

        if(sensor.reflection() >= grey):
            robot.straight(175)
            robot.turn(45)
            print("Den turner anden gang")
            Kør_Lige_ud(robot,sensor,threshold,-2)

        else:
            # "fejl lyd"
            ev3.speaker.beep()
    else:
            # "fejl lyd"
            ev3.speaker.beep()




''' Dette er en tidligere kode
 def FireGrå(DriveBase,sensor,grey, white):
    while sensor.reflection() < grey:
        robot.turn(-5)
    while sensor.reflection() >= white:
        robot.turn(-5) '''
