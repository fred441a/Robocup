def stop_på_midte(drivebase, ultra_sensore):
    while True:
        if ultra_sensore.distance() > 1368:
            drivebase.drive(100,00)
        else:
            break