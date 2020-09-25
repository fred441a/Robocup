from pybricks.parameters import Stop
from Ligeud import Kør_Lige_ud
from pybricks.tools import wait

def dreje_mod_flaske(drivebase):
    drivebase.straight(200)
    drivebase.turn(90)

#den kører frem og får flasken ind i grebet. Vi har målt at der er 8 cm fra sensor til flasken
def Kør_hen_til_flaske(DriveBase,ultra_sensor):
    while True:
        if ultra_sensor.distance() < 120:
            DriveBase.stop()
            print("afstand fundet")
            break
        else:
            DriveBase.drive(50,0)

#set openclose til tru hvis den skal åbne og false hvis den skal lukke
def løfte_flaske(Arm_Motor, openclose):
    if openclose:
        print(Arm_Motor.angle())
        Arm_Motor.run_target(200,1500, then=Stop.HOLD, wait=True)
    else:
        Arm_Motor.run_target(200,0, then=Stop.HOLD, wait=True)

def Kør_indtil_sort(drivebase,line_sensor):
    while True:
        drivebase.drive(100,0)
        if line_sensor.reflection() < 15:
            drivebase.stop()
            break
        wait(10)


def AndetSegment(drivebase,Arm_Motor,ultra_sensor,line_sensor,threshold):
    drivebase.reset()
    dreje_mod_flaske(drivebase)
    drivebase.reset()
    Kør_hen_til_flaske(drivebase,ultra_sensor)
    løfte_flaske(Arm_Motor,True)
    Kør_indtil_sort(drivebase,line_sensor)
    løfte_flaske(Arm_Motor,False)
    løfte_flaske(Arm_Motor,True)
    drivebase.straight(-drivebase.distance())
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,-2)




   



