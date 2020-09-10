def PickupFlask(motor):
    print("PIcking up")
    while motor.angle() <= 1300:
        motor.run(200)
    motor.stop()

def PutDownFlask(motor):
    print("Putting down")
    while motor.angle() > 2:
        motor.run(200)
    motor.stop()


