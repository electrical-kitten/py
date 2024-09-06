# с начала пытаемся выполнить код в Try, у нас не получается, получаем ошибку, сравниваем ее с except., и выполняем код оттуда 
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You cant divide by zero")

print("Give me two numbers, and I'll dicide them")
print("Enter q to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by zero")
    else:
        print(answer)