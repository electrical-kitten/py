class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you sneaky bastard")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery_size = 40

    def describe_battery(self):
        print(f"This car has a {self.battery_size}- kWh battery.")

my_new_car = Car('audi', 'a4', 2024)
my_used_car = Car('subaru', 'outback', 2019)
my_electric_car = ElectricCar('tesla', 'super model s', 2022)

# print(my_new_car.get_descriptive_name())
# print(my_used_car.get_descriptive_name())
# print(my_electric_car.get_descriptive_name())

# my_new_car.update_odometer(15)
# my_used_car.update_odometer(23500)

# my_new_car.read_odometer()

# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

my_electric_car.describe_battery()