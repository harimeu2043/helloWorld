class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, {self.num_doors} doors"

class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()}, {self.battery_capacity} kWh battery capacity"

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return f"{super().display_info()}, {self.payload_capacity} lbs payload capacity"

car1 = Car("Toyota", "Corolla", 2022, 4)
electric_car1 = ElectricCar("Tesla", "Model S", 2023, 4, 100)
truck1 = Truck("Ford", "F-150", 2024, 2000)

print(car1.display_info())
print(electric_car1.display_info())
print(truck1.display_info())
