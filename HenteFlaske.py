from pybricks.parameters import Stop
from Ligeud import Kør_Lige_ud
from pybricks.tools import wait

def dreje_mod_flaske(drivebase):
    drivebase.straight(230)
    drivebase.turn(90)

#den kører frem og får flasken ind i grebet. Vi har målt at der er 8 cm fra sensor til flasken
def Kør_hen_til_flaske(drivebase,ultra_sensor):
    while True:
        if ultra_sensor.distance() < 115:
            drivebase.stop()
            print("afstand fundet")
            break
        else:
            drivebase.drive(100,0)

#set openclose til tru hvis den skal åbne og false hvis den skal lukke
def løfte_flaske(Arm_Motor, openclose):
    if openclose:
        print(Arm_Motor.angle())
        Arm_Motor.run_target(300,1800)
    else:
        Arm_Motor.run_target(300,0)

def Kør_indtil_sort(drivebase,line_sensor):
    while True:
        drivebase.drive(200,0)
        if line_sensor.reflection() < 15:
            drivebase.stop()
            break
        wait(5)


def AndetSegment(drivebase,Arm_Motor,ultra_sensor,line_sensor,threshold):
    drivebase.reset()
    dreje_mod_flaske(drivebase)
    drivebase.reset()
    Kør_hen_til_flaske(drivebase,ultra_sensor)
    løfte_flaske(Arm_Motor,True)
    drivebase.straight(270)
    løfte_flaske(Arm_Motor,False)
    løfte_flaske(Arm_Motor,True)
    drivebase.straight(-drivebase.distance())
    drivebase.turn(-90)
    Kør_Lige_ud(drivebase,line_sensor,threshold,-3)




   



