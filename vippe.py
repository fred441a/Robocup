from Ligeud import Kør_Lige_ud

def TredjeSegment(drivebase,line_sensor,threshold):
    drivebase.straight(100)
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,2)
    drivebase.straight(2000)
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,2)
