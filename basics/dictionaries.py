# alien_0 = {
#     'color': 'green',
#     'points': 5
# }

# print(alien_0['color'])
# print(alien_0['points'])

# # добавляем значения в объект (словарь)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

# # изменяем значение

# alien_0['color'] = 'yellow'

# print(alien_0)

####

# alien_0 = {
#     'x_position': 0,
#     'y_position': 25,
#     'speed': 'medium',
#     'points': 5
# }
# print(f"The original position: {alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print(f"New position: {alien_0['x_position']}")

# # удаляем ключ значение

# del alien_0['points']
# print(alien_0)

#####

# get() с помощью метода, пытаемся вытянуть значение ключа, но если такого ключа в объекте нет, то вторым аргументом мы указваем то что будет отдано, вместо ошибки. Если вовсе не указать второй аргумент, то вернется none

# alien_0 = {'color': 'green', 'speed': 'slow'}

# point_value = alien_0.get('points', 'No value assigned')
# print(point_value)

##### looping #####

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# метод items() проходит по объекту и возваращает ключ и значение каждого айтема, которые мы сохраняем в переменные key и value

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']

# for name, language in favorite_languages.items():
#     print(name)
#     print(language)

# keys() метод возвращает только ключи из объекта. по дефолту for и так пройдет только по ключам, так что keys() можно не писать, но с ним лучше читается код

# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()} i see you like {language}")

##########

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# # цикл прошел по ключам в алфовитном порядке
# # for name in sorted(favorite_languages.keys()):
# #     print(f"{name.title()}, thank you for taking the poll")

# # values() метод возвращает значение объекта
# # for language in favorite_languages.values():
# #     print(language.title())

# # set() возвращает коллекцию из объекта только с уникальными занчениями
# for language in set(favorite_languages.values()):
#     print(language.title())

##### EXERCISE #####

# rivers = {
#     'volga': 'russia',
#     'nile': 'egypt',
#     'amriv': 'usa'
# }

# # for river, country in rivers.items():
# #     if country == 'usa':
# #         print(f"\nThe {river.title()} runs through {country.upper()}")
# #     else:
# #         print(f"\nThe {river.title()} runs through {country.title()}")

# for river in rivers.keys():
#     print(river.title())

# for country in rivers.values():
#     if country == 'usa':
#         print(country.upper())
#     else:
#         print(country.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# should_answer = ['anton', 'vadim', 'phil', 'sarah']

# for people in should_answer:
#     if people in favorite_languages.keys():
#         print(f"{people} thak you for youe answer")
#     if people not in favorite_languages.keys():
#         print(f"{people} you should answer the pole")

#### NESTING ####

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# # make 30 aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[:5]:
#     print(alien)
# print("...")

##### списки в объектах #####

# pizza = {
#     'crust': 'thiccc',
#     'toppings': ['mushrooms', 'extra cheese']
# }

# print(f"you ordered a {pizza['crust']
#                        } - crust pizza with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# favorite_languages = {
#     'jen': ['python', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell'],
# }

# # поскольку items() вытянул список в languages, мы можем циклом перебрать его

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favourite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

##### ОБЪЕКТЫ В ОБЪЕКТАХ ######

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }


# for user_name, user_info in users.items():
#     print(f"\nUsername: {user_name}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']

#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation {location.title()}")

##### EXERCISE #####

# friend1 = {
#     'first': 'kirill',
#     'last': 'selitskiy',
#     'age': 28,
#     'location': 'spb'
# }

# friend2 = {
#     'first': 'alexey',
#     'last': 'vlasyuk',
#     'age': 26,
#     'location': 'msc'
# }

# friend3 = {
#     'first': 'ilia',
#     'last': 'migulin',
#     'age': 25,
#     'location': 'anotherloc'
# }

# people = [friend1, friend2, friend3]

# for friend in people:
#     print(f"\nMy friend's name is {friend['first'].title()} {friend['last'].title()}, he is {
#           friend['age']} and he lives in {friend['location'].title()}")


#####

# favourite_places = {
#     'kirill': ['prison', 'tap 22'],
#     'ilia': ['russian banya', 'his home'],
#     'alexey': ['russian banya', 'futura', 'nature']
# }

# for people, places in favourite_places.items():
#     print(f"\n{people}'s favourite places are:")
#     for place in places:
#         print(f"\t{place}")

#####

cities = {
    'moscow': {
        'like_living': False,
        'country': 'russia',
        'population': 130000
    },
    'barcelona': {
        'like_living': True,
        'country': 'spain',
        'population': 200000
    },
    'tokyo': {
        'like_living': True,
        'country': 'japan',
        'population': 500000
    }
}

for city_name, city_info in cities.items():
    print(f"\nThe city is {city_name.title()}:")
    print(f"\tDo i want to live in this country?:{city_info['like_living']}")
    print(f"\tIt is located in {city_info['country'].title()} ")
    print(f'\tThe population is {city_info['population']}')

    # for details in city_info:
    #     print(f"\tDo i want to live in this country?:{details['like_living']}")
    #     print(f"\tIt is located in {details['country'].title()} ")
    #     print(f'\tThe population is {details['population']}')
