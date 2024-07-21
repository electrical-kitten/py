# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_toppings = ['mushrooms', 'onions', 'pineapple']

# for topping in requested_toppings:
#     if 'mushrooms' in topping:
#         print('yes')
#     else:
#         print('no')

# banned_users = ['andrew', 'carolina', 'david']

# user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()} you are not banned")

##### EXERCISE #####

# alien_color = 'red'

# if alien_color == 'green':
#     print('you have earned 5 points')
# if alien_color == 'red':
#     print('you have earned 5 points')

# if alien_color == 'green':
#     print('you have earned 5 points')
# elif alien_color == 'yellow':
#     print(' 10 points for you')
# elif alien_color == 'red':
#     print(" 15 points")

# age = 32

# if age < 2:
#     print('you are a baby')
# elif age >= 2 and age < 4:
#     print("your are a todler")
# elif age >= 4 and age < 13:
#     print("you are a kid")
# elif age >= 13 and age < 20:
#     print("you are a teenager")
# elif age >= 20 and age < 65:
#     print("you are an adult")
# elif age >= 65:
#     print("you are an elder")

# fruits = ['bananas', 'apples', 'oranges']

# if 'bananas' in fruits:
#     print("you really love bananas")

# if 'apples' in fruits:
#     print("you really love apples")

# if 'oranges' in fruits:
#     print("you really love oranges")

##### IF IN LISTST #####

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("sorry we are out of peppers!")
#     else:
#         print(f"adding {requested_topping}")

# print("\npizza is ready")

#####

# available_toppings = ['mushrooms', 'olives', 'green peppers',
#                       'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}")
#     else:
#         print(f"There is no {requested_topping}")

# print("\npizza is ready")

##### EXERCISE #####

# user_names = ['destroyer', 'kitten123', 'admin', 'yourmom', 'reckful']

# user_names = []

# for user_name in user_names:
#     if user_name == 'admin':
#         print(f"Hello {user_name}, would you like to see stats?")
#     else:
#         print(f"Hello {user_name}")

# if user_names == []:
#     print("we need to find some users")

#####

# current_users = ['DESTROYER', 'kitten123', 'admin',
#                  'yourmom', 'ReckFul', 'SubCultura']

# current_users_lower = [user.lower() for user in current_users]

# new_users = ['onion', 'reckful', 'conqueeftador', 'subcultura', 'serega15']

# for new_user in new_users:
#     if new_user in current_users_lower:
#         print(f"{new_user} is already taken")
#     else:
#         print(f"{new_user} is available")

numbers = list(range(1, 10))

print(numbers)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f'{number}th')
