# def greet_user(user_name):
#     print(f"Hello {user_name.title()}")


# greet_user('vlad')

# def display_message():
#     print("in this chapter i am learning functons in python")

# display_message()


# def favourite_book(title):
#     print(f"One of my favourite books is {title.title()}")

# favourite_book('flowers for eldjernon')

#########

# POSITIONAL ARGUMENTS

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet('cat', 'semyon')

# KEYWORD ARGUMENTS

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# # Этот метод передачи аргументов хорош тем, что нам не важен порядок передаваемых аргументов, так как мы четко обозначаем каждый аргумент

# describe_pet(animal_type='hamster', pet_name='harry')

# DEFAULT VALUES

# определяем дефолтный параметр 'dog', то есть при вызове фунции без параметра animal_type всегда будет передаваться dog

# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet('muhtar', 'cat')

######

# def make_shirt(text='I love python', size='l'):
#     print(f"This T-Shirt is in size {size.upper()
#                                      }, and the print says '{text}'")


# make_shirt(size='m', text='kjfadsjklafd')

# def describe_city(name, country='iceland'):

#     if country == 'usa':
#         print(f"{name.title()} is in {country.upper()}")
#     else:
#         print(f"{name.title()} is in {country.title()}")


# describe_city('moscow', 'russia')
# describe_city('random')
# describe_city('texas', 'usa')


##########################
# RETURNS

# return возвращаем значение которое произвела функция
# middle_name необязательный параметр

# def get_formated_name(first_name, last_name, middle_name=''):

#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()


# musician = get_formated_name('jimmi', 'hendrix')
# print(musician)

# musician = get_formated_name('john', 'hooker', 'lee')
# print(musician)

#################
# RETURN DICTIONARIES

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age

#     return person


# musician = build_person('jimi', 'hendrix', 27)
# print(musician)

##############

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name:\n")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

#############
# 8.6 - 8.8

# def city_country(city_name, city_country):
#     city_value = f"{city_name.title()}, {city_country.title()}"
#     return city_value


# print(city_country('moscow', 'russia'))
# print(city_country('new your', 'america'))

####

# def make_album(artist_name, album_title, songs_number=None):
#     describe_album = {
#         'artist': artist_name.title(),
#         'title': album_title.title()
#     }
#     if songs_number:
#         describe_album['songs'] = songs_number

#     return describe_album


# while True:
#     print("(input 'q' at any time to exit)")
#     name = input("\nEnter a artist name:\n")
#     if name == 'q':
#         break

#     title = input("\nEnter a album title:\n")
#     if title == 'q':
#         break

#     songs = input("\nEnter a number of songs:\n")
#     if songs == 'q':
#         break

#     final_album = make_album(name, title, songs)

#     print(final_album)

#################################
# LIST

# user_names = ['hannah', 'ty', 'margot']


# def greet_users(names):

#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)


# greet_users(user_names)

#####

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahidron']
# completed_models = []


# def print_models(unprinted_designs, completed_models):

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)


# # [:] с этой нотацией при вызове функции мы передаем не оригинал списка а его копию, что бы не оригинал не изменился в ходе выполнения. Но это лучше использовать если это прям действительно нужно, ибо испльзуется память

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

#################
# 8.9-8.11

# messages = ['hello', 'goodbye', 'go fuck yourself']
# sent_messages = []


# def show_messages(messages):
#     for message in messages:
#         print(message)


# def send_messages(messages, sent_messages):
#     while messages:
#         sending = messages.pop()
#         print(f"Sending message: {sending}")
#         sent_messages.append(sending)


# send_messages(messages[:], sent_messages)

# print(messages)
# print(sent_messages)

###############

# Произвольные аргументы в функиях. * позволяет вписывать неограниченое количество аргументов
# записвывается чаще как *args


# def make_pizza(size, *toppings):
#     print(f"\Making a {size}-cm pizza with the following topings:")
#     for topping in toppings:
#         print(topping)


# make_pizza(22, 'pepperoni')
# make_pizza(16, 'mushrooms', 'peppers', 'cheese')

# Произвольные ключ-значения с помощью **
# записываются чаще как *kwargs

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile(
#     'albert', 'einstein', location='princeton', field='phisycs')

# print(user_profile)

################
# 8.12 - 8.14

# def sandwich_ingredients(*args):
#     print(f"Sandwich will contain these items: {args}")


# sandwich_ingredients('mozarella', 'pesto', 'prostiuto')
# sandwich_ingredients('cheese', 'olive oil', 'roast beef', 'onions')

###

# def person_profile(first, last, **kwargs):
#     kwargs['first_name'] = first
#     kwargs['last_name'] = last
#     return kwargs


# user_info = person_profile('vladislav', 'begunkov',
#                            age=32, sex='male', nationality='russian')

# print(user_info)

####

# def car_information(manufacture, model, **car_info):
#     make_car = {
#         'manufacturer': manufacture.title(),
#         'model': model.title(),
#     }
#     for info, value in car_info.items():
#         make_car[info] = value

#     return make_car


# car = car_information('subaru', 'outback', color='blue', tow_package=True)

# print(car)

#####################

# STORING FUNCTIONS IN MODULES
