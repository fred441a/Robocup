from Ligeud import Kør_Lige_ud






def FireGrå(robot, sensor, grey, white):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-22)
    print("Den turner første gang")

    if(sensor.reflection() >= white):
        robot.drive(175,0)

        if(sensor.reflection() >= white):
            robot.drive(175,0)
            robot.turn(20)
            print("Den turner")
            Kør_Lige_ud(robot,sensor,threshold,-2)

        else:
            # "fejl lyd"
            ev3.speaker.beep()
    else:
        # "fejl lyd"
            ev3.speaker.beep()

def FireGråAlt(robot, sensor, grey, white):
    threshold = (grey+white)/2
    robot.straight(500)
    robot.turn(-22)
    print("Den turner første gang")
    robot.straight(200)

    while(sensor.reflection() >= white):
        robot.drive(175,0)

        if(sensor.reflection() < white):
            robot.stop()
            break
        wait(10)
    robot.turn(20)
    print("Den turner")
    Kør_Lige_ud(robot,sensor,threshold,-2)



''' Dette er en tidligere kode
 def FireGrå(DriveBase,sensor,grey, white):
    while sensor.reflection() < grey:
        robot.turn(-5)
    while sensor.reflection() >= white:
        robot.turn(-5) '''
