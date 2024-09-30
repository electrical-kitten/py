from name_test import get_fromatted_name

print("Enter 'q' ata any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_fromatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

   # middle = input("Please give me a a middle name: ")
    # if first == 'q':
    #     break