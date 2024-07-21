# bicycles = ['trek', 'cannondale', 'redline', 'specialized',]

# print(bicycles[1].title())
# print(bicycles[-1].upper())
# print(f'my first bicycle wa a {bicycles[1].title()}')

# motorcycles = ['honda', 'yamaha', 'suzuki']

# motorcycles[0] = 'ducati'  # заменить первый элемент списка
# motorcycles.append('ducati')  # в конец списка
# motorcycles.insert(0, 'ducati')  # вставить значение по указаному индексу

# del motorcycles[0]

# # удаляем последний элемент из списка и можем созранить его в переменной
# popped_moto = motorcycles.pop()
# last_owned = motorcycles.pop()
# first_owned = motorcycles.pop(0)

# # удаляет значение по совпадению названия, но только когда оно встречается один раз
# motorcycles.remove('yamaha')
# too_expensive = 'yamaha'
# motorcycles.remove(too_expensive)

# print(motorcycles)
# print(last_owned)
# print(first_owned)
# print(popped_moto)

# ##########################

# guests = ['joe rogan', 'jordan peterson', 'andrew huberman']

# print(guests)

# print(f'Hey {guests[0].title()}')
# print(f'Hey {guests[1].title()}')
# print(f'Hey {guests[-1].title()}\n')

# excluded = 'jordan peterson'

# print(f'{excluded.title()} cant make it\n')

# guests[1] = 'action bronson'

# print(f'Hey {guests[0].title()}')
# print(f'Hey {guests[1].title()} is the new guest')
# print(f'Hey {guests[-1].title()}')

# print(guests)

# print('\nFound a bigger table\n')

# guests.insert(0, 'jimmy hendricks')
# guests.insert(1, 'jony cash')
# guests.append('bob dyllan')

# print(f'Hey {guests[0].title()} is the new gurst')
# print(f'Hey {guests[1].title()} is the new guest')
# print(f'Hey {guests[2].title()}')
# print(f'Hey {guests[3].title()}')
# print(f'Hey {guests[4].title()}')
# print(f'Hey {guests[-1].title()} is the new guest')

# print(guests)

# print('\nChange of plans, I can only invite 2 people\n')

# print(f'{guests.pop(0).title()} im sorry')
# print(f'{guests.pop(0).title()} im sorry')
# print(f'{guests.pop(2).title()} im sorry')
# print(f'{guests.pop(2).title()} im sorry')

# print(f'{guests[0]}, {guests[1]} you are still invited!')

# print(guests)

# del guests[0]
# del guests[0]

# print(guests)

# ####### SORTING #######

# cars = ['bmw', 'audi', 'toyota', 'subaru']

# cars.sort()  # изменяет порядок списка в алфовитном порядке перманентно
# cars.sort(reverse=True)  # reverse = True обратный алфавитный порядок

# print(cars)

# # sorted() сортирует в алфавитном порядке, но не изменяет оригинальный список
# print(sorted(cars))

# cars.reverse()  # меняет порядок списка в обратный
# print(cars)

# len(cars)  # длинна списка

# ###### EXERCISSE #######

# countries = ['japan', 'germany', 'new zeland', 'australia', 'south korea']

# print(countries)
# print(sorted(countries))
# print(sorted(countries, reverse=True))

# countries.reverse()
# countries.reverse()

# countries.sort()
# countries.sort(reverse=True)
# print(countries)

# #####  WORKING WITH LISTS #####

# magicians = ['alice', 'david', 'carolina']

# # цикл проходит по каждому элементу списка и присваивает его к временной переменной magician
# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick')
#     print(f'I cant wait to see your next trick {magician.title()}')

####### exercise ######

# favourite_pizzas = ['pepperoni', '4 cheeses', 'putanesca']

# for pizza in favourite_pizzas:
#     print(f"I like {pizza} pizza")

# print("\nI really fucking love pizza!")

# predators = ['tiger', 'grizzly', 'wolf', 'jaguar']

# for predator in predators:
#     print(f"{predator} would deffinetly kill you")

# print("They are all deadly killers!")

##### NUMERICAL LISTS #####

# for value in range(1, 6): # перебирает указанный диапазон чисел от 1 до 5
#     print(value)

# создаем списко чисел с помощью метода list() и range()

# numbers = list(range(1, 6))
# print(numbers)

# задаем рэйндж от 2 до 11 и третим аргументом задаем шаг для метода.
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

######################

# squares = []

# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

#####################

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# print(min(digits))
# print(max(digits))
# print(sum(digits))

###### list comprehensions  #####

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

##### EXERCISE #####

# for value in range(1, 21):
#     print(value)

# big_fucking_list = list(range(1, 1_000_000))


# print(min(big_fucking_list))
# print(max(big_fucking_list))
# print(sum(big_fucking_list))


# for value in big_fucking_list:
#     print(value)

# bfl_odd = list(range(1, 1_000_000, 2))

# for value in bfl_odd:
#     print(value)

# multiples = list(range(3, 30))

# for value in multiples:
#     multiple = value * 3
#     print(multiple)

# cubes = list(range(1, 10))

# for value in cubes:
#     cube = value ** 3
#     print(cube)

# cubes = [value ** 3 for value in range(1, 10)]
# print(cubes)

########  PARTS OF A LIST ##########

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# часть списка
# print(players[0:3])

# # если не указать первый аргумент, то список начнется с начала автоматом, что так же работает и наоборот если не указать последний индекс
# print(players[:4])
# print(players[2:])
# print(players[-3:])

# for player in players[:3]:
#     print(player.title())
# print('first 3 players from the list')


#####  COPY LISTS #####

# my_foods = ['pizze', 'falafel', 'carrot cake']

# # копируем список
# friends_foods = my_foods[:]

# my_foods.append('burgers')
# friends_foods.append('ice cream')

# print(my_foods)
# print(friends_foods)

##### EXERCISE #####

# my_foods = ['pizze', 'falafel', 'carrot cake', 'pasta', 'sushi']

# print(f"The first three items are: {my_foods[:3]}")
# print(f"The first three items are: {my_foods[1:4]}")
# print(f"The last thre items are: {my_foods[-3:]}")

# favourite_pizzas = ['pepperoni', '4 cheeses', 'putanesca']

# friend_pizzas = favourite_pizzas[:]

# favourite_pizzas.append('diabola')
# friend_pizzas.append('margharita')

# print(f"My pizzas are:")

# for my_pizza in favourite_pizzas:
#     print(my_pizza)

# print("Friend pizzas are:")

# for friend_pizza in friend_pizzas:
#     print(friend_pizza)

####### TUPLES AKA КОРТЕЖИ ########

# кортежи это неизменяемые списки
# обозначаются скобками и считаются кортежами если присутствует запятая

# dimensions = (200, 50)

# ошибка
# dimensions[0] = 50

# print(type(dimensions))
# print(dimensions[0])
# print(dimensions[1])

# мы не можем изменять существующий кортеж(добавлять, удалаять значения), но мы можем переназначить кортеж полностью
# dimensions = (200, 50)


# print('these are old')
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)

# print('\nThese are new')
# for dimension in dimensions:
#     print(dimension)

###### EXERCISE ######

foods = ('burger', 'steak', 'pasta', 'salad', 'pate')

for food in foods:
    print(food)

foods = ('lazagna', 'steak', 'pasta', 'salad', 'duck')

for food in foods:
    print(food)
