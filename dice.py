from random import randint, choice

class Die:
    def __init__(self, sides = 6):

        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)

d6 = Die()
d10 = Die(10)
d20 = Die(20)

# for roll in range(1,7):
#     d6.roll_die()

for roll in range(1, 11):
    d10.roll_die()

for roll in range(1, 21):
    d20.roll_die()
