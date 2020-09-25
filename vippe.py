from Ligeud import Kør_Lige_ud

def TredjeSegment(drivebase,line_sensor,threshold):
    drivebase.straight(200)
    drivebase.turn(-90)
    drivebase.straight(2750)
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,-2)
