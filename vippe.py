from Ligeud import Kør_Lige_ud, Kør_Lige_ud_Ind_TIL

def TredjeSegment(drivebase,line_sensor,threshold):
    drivebase.straight(200)
    drivebase.turn(-85)
    drivebase.straight(2780)
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,2)

def TredjeSegment_alt(drivebase,line_sensor,threshold,hvid,grå):
    drivebase.straight(200)
    drivebase.turn(-85)
    Kør_Lige_ud(drivebase,line_sensor,threshold,-2)
    drivebase.straight(400)
    Kør_Lige_ud_Ind_TIL(drivebase,line_sensor,threshold,-2,10000)
    drivebase.straight(400)
    Kør_Lige_ud(drivebase,line_sensor,threshold,-10)

#    if line_sensor.reflection() >= hvid:
#        while True:
#            drivebase.drive(-100,0)
#            if line_sensor.reflection() <= grå:
#                drivebase.stop()
#                break
#    else:
#        print("LÆNGERE!")
#    drivebase.turn(-90)
