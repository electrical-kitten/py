class Restaurant:

    def __init__ (self, restaurant_name, cuisine_type):

        self.rest_name = restaurant_name.title()
        self.cuisine = cuisine_type
        self.clients_served = 0

    def describe_restaurant(self):
        print(f"{self.rest_name} is now open")

    def set_number_served(self, clients_number):
        self.clients_served = clients_number

first_rest = Restaurant('saviv', 'isralian')
second_rest = Restaurant('fahrenheit', 'european')


first_rest.describe_restaurant()
second_rest.describe_restaurant()

print(first_rest.clients_served)
first_rest.set_number_served(19)
print(first_rest.clients_served)