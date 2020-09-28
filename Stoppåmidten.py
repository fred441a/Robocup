from Ligeud import Kør_Lige_ud_midten

def stop_på_midten(DriveBase, ultra_sensor):
    Kør_Lige_ud_midten(robot,line_sensor,threshold,-3, ultra_sensor)

    drivebase.reset()
    robot.straight(-1275)
    robot.turn(-90)
    robot.straight(30)


    
    

    
    