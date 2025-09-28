from vehicles import Vehicle, Bus

if __name__ == '__main__':

    print("Sample #1: Abstract Vehicle")
    vehicle = Vehicle("Generic Vehicle", 2025)
    vehicle.drive(100)
    vehicle.stop()
    print("")

    print("Sample #2: Bus and Bicycle, more specific Vehicles")
    bus = Bus("Citaro O530G", 2020, 100)
    bus.drive(80)
    bus.stop()
    bus.open_doors(1)
    bus.open_doors(2)
    print("")