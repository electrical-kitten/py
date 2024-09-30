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

class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        print(f"Admin {self.privileges[0]}, {self.privileges[2]}, {self.privileges[1]}")

class Admin:
    def __init__(self):

        self.admin_priv = Privileges()

user1 = User('Vladislav', 'Begunkov', 32, 'example@gmail.com')
user2 = User('Bla', 'Blakov', 40, 'example2222@gmail.com')
admin = Admin()

# user1.describe_user()
# user2.describe_user()

# user1.greet_user()
# user2.greet_user()

# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)

admin.admin_priv.show_privileges()