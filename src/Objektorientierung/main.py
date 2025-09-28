import random

from vehicles import Vehicle, Bus, Bicycle, Tram

if __name__ == '__main__':

    vehicles: list[Vehicle] = list()
    vehicles.append(Bus("Citaro O530G", 2020, 100))
    vehicles.append(Bicycle("KTM", 2024, True))
    vehicles.append(Bus("Citaro LE", 2019, 50))
    vehicles.append(Tram("GT8-80C", 1996, True))

    for vehicle in vehicles:

        speed: int = random.randint(20, 50)
        vehicle.drive(speed)

        if isinstance(vehicle, Bus):
            vehicle.stop()
            vehicle.open_doors(1)
            vehicle.open_doors(2)

        if isinstance(vehicle, Bicycle):
            vehicle.set_driver_activity(False)

