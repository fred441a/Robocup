from Ligeud import Kør_Lige_ud

def stop_på_midten(DriveBase, ultra_sensor):
    Kør_Lige_ud(robot,line_sensor,threshold,-3)
    if ultra_sensor.distance() < 150:
            DriveBase.stop()
            print("afstand fundet")
            break
    drivebase.reset()
    robot.straight(-1275)
    robot.turn(-90)
    robot.straight(30)


    
    

    
    