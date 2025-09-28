class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self, speed_in_kmh):
        print(f"The {self.model} is driving at {speed_in_kmh} km/h.")

    def stop(self):
        print(f"The {self.model} has stopped.")


class Bus(Vehicle):
    def __init__(self, model, year, capacity):
        super().__init__(model, year)

        self.capacity = capacity

    def drive(self, speed_in_kmh):
        print(f"The bus {self.model} with capacity {self.capacity} is driving at {speed_in_kmh} km/h.")

    def stop(self):
        print(f"The bus {self.model} has stopped.")

    def open_doors(self, door_number):
        print(f"The bus {self.model} opens door number {door_number}.")

    def close_doors(self, door_number):
        print(f"The bus {self.model} closes door number {door_number}.")