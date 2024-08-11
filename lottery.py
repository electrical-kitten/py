from random import randint, choice

lottery = ['a', 'b', 'c', 'd', 'e', 29, 20, 79, 43, 100, 46, 72, 37, 60, 73]

# lottery = ['a', 'b', 1, 2]

winning_ticket = [46, 'c', 'a', 72]
# winning_ticket = [2, 'b', 'a', 1]
my_ticket = []
attempts = 0

def generate_combination():

    for i in range (1, 5):
        my_ticket.append(choice(lottery))

while my_ticket != winning_ticket:

    generate_combination()

    if my_ticket == winning_ticket:
        print("************\n")
        print("You Won!")
        print(f"\n Winning combination - {winning_ticket}")
        print(f"\n Your combination - {my_ticket}")
        print(f"It took {attempts} - attempts")
        print("\n************")

        break
    else:
        print(f"\n Winning combination - {winning_ticket}")
        print(f"\n Your combination - {my_ticket}")
        print("no luck") 
        my_ticket = []
        attempts += 1
 


# print(winning_ticket)
