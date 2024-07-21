# названия классов пишутся с заглавной буквы
class Dog:

    """моделируем поведение собаки"""

    #
    def __init__(self, name, age):
        # инициализация атрибутов
        self.name = name
        self.age = age

    def sit(self):
        # симуляция команды сидеть
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


# инстанс класса Dog с атрибутами name и age
my_dog = Dog('Bruno', 7)
my_other_dog = Dog('muhtar', 10)

# после того как у нас появился инстанс класса, мы можем использовать его атрибуты
# my_dog.name
# my_other_dog.age


print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} yeaers old")
print(f"My other dog's name is {my_other_dog.name}")

# и послек того как появился инстанс, мы можем использовать другие методы класса
my_dog.sit()
my_dog.roll_over()

my_other_dog.sit()
my_other_dog.roll_over()
