# prompt = "\nPlease enter hte name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# current_number = 0

# while current_number < 10:
#     current_number += 1

# age = int(input("how old are you?"))

##################

# user_car = input('What kind of car do you want to rent?')
# print(f"let me se if I can find you a {user_car}")

# people_amount = int(input("How many people are in your dining group???\n"))

# if people_amount > 8:
#     print("you will have to wait to be seated")
# else:
#     print("your table is ready")

##### While loops #####

# current_number = 0

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

##### parrot #####

# prompt = "\nTell me something, and i will repert it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# active = True

# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

#######

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

#####

# current_number = 0

# while current_number < 10:
#     current_number += 1
#     # если if true то continue говорит начать следующую итерацию цикла, недоходя до rint
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

##################
# 7.4 - 7.7

# prompt = "\nEnter toppings you want on your pizza!"
# prompt += "\nType 'quit' when you are done.\n"

# user_toppings = []

# while True:

#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         user_toppings.append(topping)
#         print(f"Added {topping.title()} to your list of toppings")

# print(user_toppings)

######

# prompt = "\nWhat is your age?\n"
# quit_prompt = "\nType 'quit' if you want to exit, type 'yes' if you want to continue"

# while True:
#     age = int(input(prompt))

#     if age < 3:
#         print("for you ticket is free")
#     elif age >= 3 and age <= 12:
#         print("the price will be $10")
#     elif age > 12:
#         print("ticket price will be  $15")

#     end_loop = input(quit_prompt)

#     if end_loop.lower() == 'yes':
#         continue
#     if end_loop.lower() == 'quit':
#         break

##################

# unconfirmed_users = ['alice', 'brian', 'candance']
# confirmed_users = []

# while unconfirmed_users:
#     # удаляем имя из списка и сохраняем в переменную
#     current_user = unconfirmed_users.pop()

#     print(f"verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print(confirmed_users)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

################

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

############

# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name?\n")
#     response = input("\nWhat would you like to eat?\n")

#     responses[name] = response

#     repeat = input("would you like to let another peson respond?(yes/no)")

#     if repeat == 'no':
#         polling_active = False

# print("\n--- Poll Results ---")

# print(responses)

# for name, response in responses.items():
#     print(f"{name.title()} would like to eat {response}")

#####################
# 7.8 - 7.10

# sandwich_orders = [
#     'spicy italian', 'pastrami', 'russian openface', 'pastrami', 'blt', 'club', 'pastrami'
# ]

# finished_sandwiches = []

# print("We are out of pasrami sandwiches")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:

#     order = sandwich_orders.pop()

#     print(f"I made your {order.title()} sandwich!")

#     finished_sandwiches.append(order)

# for sandwich in finished_sandwiches:
#     print(sandwich.title())

#####

prompt_name = "\nEnter your name:\n"
prompt_location = "\nEnter your dream location:\n"

dream_location = {}

while True:

    user_name = input(prompt_name)
    user_location = input(prompt_location)

    dream_location[user_name] = user_location

    another_person = input("would you like to ask another person?(yes/no)")

    if another_person == 'no':
        break

print(dream_location)
