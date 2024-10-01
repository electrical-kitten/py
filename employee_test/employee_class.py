class Employee:

    def __init__(self, first_n, last_n, salary):

        self.first_name = first_n.title()
        self.last_name = last_n.title()
        self.anual_salary = salary

    def give_raise(self, raise_amount=5000):
        self.anual_salary += raise_amount
        print(self.anual_salary)
