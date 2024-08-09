class User:

    def __init__ (self, first_name, last_name, age, email):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, age: {self.age}, email: {self.email} ")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome to our website!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Vladislav', 'Begunkov', 32, 'example@gmail.com')
user2 = User('Bla', 'Blakov', 40, 'example2222@gmail.com')

# user1.describe_user()
# user2.describe_user()

# user1.greet_user()
# user2.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
