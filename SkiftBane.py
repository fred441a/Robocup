def Skift_linje_Højre(DriveBase,sensor,grey):
    DriveBase.turn(60)
    DriveBase.straight(200)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        DriveBase.drive(200,0)
    DriveBase.stop()
    DriveBase.turn(-45)

def Skift_linje_Venstre(DriveBase,sensor,grey):
    DriveBase.turn(-60)
    DriveBase.straight(200)
    print(grey)
    while sensor.reflection() > grey:
        print(sensor.reflection())
        DriveBase.drive(200,0)
    DriveBase.stop()
    DriveBase.turn(50)