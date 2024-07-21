class User:

    def __init__(self, first_name, last_name, age, ocupation):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_age = age
        self.user_ocupation = ocupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"Hello {self.first_name} {self.last_name}. You work as a {
              self.user_age} and you are {self.user_ocupation}")

    def greet_user(self):
        print(f"Well {
              self.first_name}, classes in python are complicated but interesting. Am I right?")

    def increment_login_attempts(self):
        """инкремент попыток входа"""

        self.login_attempts += 1

    def reset_login_attempts(self):
        """обнуление попыток входа"""

        self.login_attempts = 0


# myself = User('vladislav', 'begunkov', 'QA-engeneer', 32)
# kirill = User('kirill', 'selitskiy', 'inmate', 29)

# myself.describe_user()
# myself.greet_user()

# kirill.describe_user()
# kirill.greet_user()

myself = User('vladislav', 'begunkov', 'QA-engeneer', 32)

myself.increment_login_attempts()
myself.increment_login_attempts()
myself.increment_login_attempts()
myself.increment_login_attempts()
print(myself.login_attempts)

myself.reset_login_attempts()
print(myself.login_attempts)
