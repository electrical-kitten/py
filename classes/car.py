class Car:
    """a simple attempt to reperesetn a car"""

    def __init__(self, make, model, year):
        """initialise attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # можем создать атрибут который не передается в праметрах метода инит
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    # изменяем атрибут через метод
    def update_odometer(self, mileage):
        """
        меняем значение одометра на указанное
        непозволяем внести изменения если новое значение ниже предыдущего

        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElecticCar(Car):

    def __init__(self, make, model, year):
        # инициализация атрибутов родительского класса
        super().__init__(make, model, year)


my_tesla = ElecticCar('tesla', 'supermodel', 2020)

print(my_tesla.get_descriptive_name())

# my_new_car = Car('audi', 'a4', 2024)

# print(my_new_car.get_descriptive_name())

# # изменяем атрибут напрямую через обращение к нему
# # my_new_car.odometer_reading = 23

# # изменяем через метод
# my_new_car.update_odometer(50)

# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
