# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):

#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f"Welcome to {self.restaurant_name.title()
#                             }! We serve {self.cuisine_type} cuisine!")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name.title()} is open!")

#     def set_number_served(self):
#         """посмотреть количество обслуженых клиентов"""

#         print(f"There are {self.number_served} guests served")

#     def increment_number_served(self, number):
#         """прибавить количество обслуженых гостей"""

#         self.number_served += number

# # first_restaurant = Restaurant('saviv', 'isralian')
# # second_rest = Restaurant('futura', 'european')
# # third_rest = Restaurant('22cm', 'italian')

# # first_restaurant.describe_restaurant()
# # first_restaurant.open_restaurant()

# # second_rest.describe_restaurant()
# # third_rest.describe_restaurant()


# restaurant = Restaurant('saviv', 'isralian')
# restaurant.number_served = 79
# restaurant.set_number_served()
# restaurant.increment_number_served(10)
# restaurant.set_number_served()
