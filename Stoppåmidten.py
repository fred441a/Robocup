from Ligeud import Kør_Lige_ud_midten , Kør_Lige_ud_Ind_TIL_Langsomt

def stop_på_midten(robot, line_sensor, ultra_sensor, threshold):
        robot.turn(35)
        robot.straight(350)
        Kør_Lige_ud_Ind_TIL_Langsomt(robot,line_sensor,threshold, -1,2000)
        Kør_Lige_ud_midten(robot, line_sensor,threshold,-5, ultra_sensor)
        robot.reset()
        robot.straight(-1800)
        robot.turn(-100)
        robot.straight(272)


    
    

    
    