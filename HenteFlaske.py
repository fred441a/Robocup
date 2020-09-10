def dreje_mod_flaske(drivebase):
    drivebase.straight(200)
    drivebase.turn(90)

#den kører frem og får flasken ind i grebet. Vi har målt at der er 8 cm fra sensor til flasken
def Kør_hen_til_flaske(drivebase,ultra_sensor):
    while ultra_sensor.distance < 80:
        DRIVE_SPEED = 200
    DriveBase.stop()
    print("STOP")

# når den er openclose = true så er armen i neutral position i bunden med armene åbne
openclose = True

def løfte_flaske(Arm_Motor):
    if openclose == True:
        print(Arm_Motor.angle())
        Arm_Motor.turn(1310)
        openclose = False
    else:
        Arm_Motor.turn(-1310)
        openclose = True
   



