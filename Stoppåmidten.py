from Ligeud import Kør_Lige_ud_midten

def stop_på_midten(robot, line_sensor, ultra_sensor, threshold):
        robot.turn(35)
        robot.straight(350)
        Kør_Lige_ud_midten(robot, line_sensor,threshold,-4, ultra_sensor)
        robot.reset()
        robot.straight(-1800)
        robot.turn(-100)
        robot.straight(272)


    
    

    
    