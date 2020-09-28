from Ligeud import Kør_Lige_ud

def TredjeSegment(drivebase,line_sensor,threshold):
    drivebase.straight(200)
    drivebase.turn(-85)
    drivebase.straight(2780)
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,2)

def TredjeSegment_alt(drivebase,line_sensor,threshold):
    drivebase.straight(200)
    drivebase.turn(-85)
    drivebase.straight(2780)
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,2)
