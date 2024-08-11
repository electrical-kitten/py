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

    def fill_gas_tank(self):
        print("Gas tank is now full")
    

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}- kWh battery.")

    def get_range(self):

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go abut {range} miles on a full charge")

    def upgrade_battery(self):

        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery_size = 40
        self.battery = Battery()

    def fill_gas_tank(self):
        print("this car doesnt have a gas tank")

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

# my_electric_car.describe_battery()

# my_used_car.fill_gas_tank()
# my_electric_car.fill_gas_tank()

# my_electric_car.battery.describe_battery()
# my_electric_car.battery.get_range()

# my_electric_car.battery.upgrade_battery()

# my_electric_car.battery.describe_battery()
# my_electric_car.battery.get_range()