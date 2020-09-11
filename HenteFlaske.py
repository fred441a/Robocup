from pybricks.parameters import Stop
def dreje_mod_flaske(drivebase):
    drivebase.straight(200)
    drivebase.turn(90)

#den kører frem og får flasken ind i grebet. Vi har målt at der er 8 cm fra sensor til flasken
def Kør_hen_til_flaske(drivebase,ultra_sensor):
    while ultra_sensor.distance() < 80:
        DriveBase.drive(200)
    DriveBase.stop()
    print("STOP")

#set openclose til tru hvis den skal åbne og false hvis den skal lukke
def løfte_flaske(Arm_Motor, openclose):
    if openclose:
        print(Arm_Motor.angle())
        Arm_Motor.run_target(200,1300, then=Stop.HOLD, wait=True)
    else:
        Arm_Motor.run_target(200,-1300, then=Stop.HOLD, wait=True)
   



