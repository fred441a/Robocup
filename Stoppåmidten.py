def stop_på_midten(DriveBase, ultra_sensor):
    while True:
        if ultra_sensor.distance() > 1368:
            DriveBase.drive(100,0)
        else:
            break