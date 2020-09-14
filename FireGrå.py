from Ligeud import Kør_Lige_ud

int lineDist = 200

def FireGråSekment(DriveBase, sensor, grey, white)
    robot.straight(500)
    robot.turn(-45)

    if(sensor.reflection() > grey)
        drive(500,0)
    else
        straight(lineDist)
            if(sensor.reflection() > grey)
                drive(500,0)
            else
                Kør_Lige_ud(robot,line_sensor,threshold,-2)
                Kør_Lige_ud(robot,line_sensor,threshold,-2)



'''    def FireGrå(DriveBase,sensor,grey, white):
    while sensor.reflection() < grey:
        robot.turn(-5)
    while sensor.reflection() >= white:
        robot.turn(-5) '''
