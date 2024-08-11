class Restaurant:

    def __init__ (self, restaurant_name, cuisine_type):

        self.rest_name = restaurant_name.title()
        self.cuisine = cuisine_type
        self.clients_served = 0

    def describe_restaurant(self):
        print(f"{self.rest_name} is now open")

    def set_number_served(self, clients_number):
        self.clients_served = clients_number
        
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)

        self.flavours = [] 

    def get_flavours(self):
        # print(f"we have {self.flavours[0]}, {self.flavours[1]}, {self.flavours[2]} icecream flavours!")
        for flavor in self.flavours:
            print(f"- {flavor.title()}")

first_rest = Restaurant('saviv', 'isralian')
second_rest = Restaurant('fahrenheit', 'european')
big_one = IceCreamStand('The Big One')
big_one.flavours = ['vanilla', 'chocolate', 'black cherry']

first_rest.describe_restaurant()
second_rest.describe_restaurant()

print(first_rest.clients_served)
first_rest.set_number_served(19)
print(first_rest.clients_served)

big_one.describe_restaurant()
big_one.get_flavours()
