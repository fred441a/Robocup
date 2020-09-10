def dreje_mod_flaske(drivebase,line_sensor,grey):
    DriveBase.straight(200)
    DriveBase.turn(90)

#den kører frem og får flasken ind i grebet. Vi har målt at der er 8 cm fra sensor til flasken
def Kør_hen_til_flaske(drivebase,ultra_sensor):
    while ultra_sensor.distance < 80:
        DRIVE_SPEED = 200

    DriveBase.stop()
    print("STOP")

# når den er openclose = true så er armen i neutral position i bunden med armene åbne
openclose = True

def løfte_flaske(drivebase):
    if openclose = True:
        print(Arm_Motor.angle())
        DriveBase.turn(1310)
        openclose = False
        else:
        DriveBase.turn(-1310)
        openclose = True
    DriveBase.stop()
   



