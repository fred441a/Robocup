from pybricks.parameters import Stop
def dreje_mod_flaske(drivebase):
    drivebase.straight(200)
    drivebase.turn(90)

#den kører frem og får flasken ind i grebet. Vi har målt at der er 8 cm fra sensor til flasken
def Kør_hen_til_flaske(DriveBase,ultra_sensor):
    while True:
        if ultra_sensor.distance() < 93:
            DriveBase.stop()
            print("afstand fundet")
            break
        else:
            DriveBase.drive(50,0)

#set openclose til tru hvis den skal åbne og false hvis den skal lukke
def løfte_flaske(Arm_Motor, openclose):
    if openclose:
        print(Arm_Motor.angle())
        Arm_Motor.run_target(200,1300, then=Stop.HOLD, wait=True)
    else:
<<<<<<< HEAD
        Arm_Motor.run_target(200,-1300, then=Stop.HOLD, wait=True)

def sænk_flaske(Arm_Motor, openclose):
    
=======
        Arm_Motor.run_target(200,0, then=Stop.HOLD, wait=True)
>>>>>>> 23c181d8d97b0af7ed2556e6bb90f7adec0857e4
   



