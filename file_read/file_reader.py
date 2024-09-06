from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy:\n")

if birthday in pi_string:
    print("your b day appears in the first million digits of pi")
else:
    print("it does not appear in the first million")

# contents = contents.rstrip()
# print(contents)

# print(f"{pi_string[:52]}")
# print(len(pi_string))