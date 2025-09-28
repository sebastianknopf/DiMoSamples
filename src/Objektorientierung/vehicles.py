from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, model: str, year: int):
        self.model: str = model
        self.year: int = year

    @abstractmethod
    def drive(self, speed_in_kmh: int):
        pass

    @abstractmethod
    def stop(self):
        pass


class Bus(Vehicle):
    def __init__(self, model: str, year: int, capacity: int, num_doors: int = 2):
        super().__init__(model, year)

        self.capacity: int = capacity
        self.num_doors: int = num_doors

    def drive(self, speed_in_kmh: int = 30):
        print(f"The bus {self.model} with capacity {self.capacity} is driving at {speed_in_kmh} km/h.")

    def stop(self):
        print(f"The bus {self.model} has stopped.")

    def open_doors(self, door_number: int):
        if door_number < 1 or door_number > self.num_doors:
            print(f"The bus {self.model} has only {self.num_doors} doors. Cannot open door number {door_number}.")
        else:
            print(f"The bus {self.model} opens door number {door_number}.")

    def close_doors(self, door_number: int):
        if door_number < 1 or door_number > self.num_doors:
            print(f"The bus {self.model} has only {self.num_doors} doors. Cannot close door number {door_number}.")
        else:
            print(f"The bus {self.model} closes door number {door_number}.")

class Bicycle(Vehicle):
    def __init__(self, model: str, year: int, is_sitting_on: bool = False):
        super().__init__(model, year)

        self._is_sitting_on: bool = is_sitting_on

    def drive(self, speed_in_kmh: int):
        if not self._is_sitting_on:
            print(f"Driver is not sitting on the bicycle. Cannot start driving.")
        else:
            if speed_in_kmh > 45:
                speed_in_kmh = 45

            print(f"The bicycle {self.model} is driving at {speed_in_kmh} km/h.")

    def stop(self):
        print(f"The bus {self.model} has stopped.")

    def set_driver_activity(self, is_sitting_on: bool):
        self._is_sitting_on = is_sitting_on

class Tram(Vehicle):
    def __init__(self, model: str, year: int, is_autonomous: bool = False):
        super().__init__(model, year)

        self._is_autonomous: bool = is_autonomous

    def drive(self, speed_in_kmh: int):
        if self._is_autonomous:
            print(f"The tram {self.model} is driving autonomously with {speed_in_kmh} km/h.")
        else:
            print(f"The tram {self.model} is driving manually with {speed_in_kmh} km/h.")

    def stop(self):
        print(f"The tram {self.model} has stopped.")