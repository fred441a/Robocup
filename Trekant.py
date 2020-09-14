# follow line until black cross line (use def kør_lige_ud)

# first turn
def indtil_hurdle():
    DriveBase.straight(50)
    DriveBase.turn(-45)
    DriveBase.stop()

# drive until wall detected
def første_væg():
    while True:
        # Begin driving forward at 100 millimeters per second.
        robot.reset_angle(0)
        robot.drive(100, 0)
        # Wait until an obstacle is detected. This is done by repeatedly
        # doing nothing (waiting for 5 milliseconds) while the measured
        # distance is still greater than 300 mm.
        while ultra_sensor.distance() > 40:
            wait(5)
        længde = robot.angle()
        # Turn right by 90 degrees
        robot.turn(90)

def væk_igen():
    while True:
        # Begin driving forward at 100 millimeters per second.
        robot.reset_angle(0)
        robot.drive(100, 0)
        # Wait until an obstacle is detected. This is done by repeatedly
        # doing nothing (waiting for 5 milliseconds) while the measured
        # distance is still greater than 300 mm.
        while robot.angle() > længde:
            wait(5)
        # Turn right by 90 degrees
        robot.turn(-45)

def ret_ind():
    while True:
        robot.drive(200,0)
        Kør_Lige_ud(robot,line_sensor,threshold,-2)