from pathlib import Path

guest_book = Path('guest_book.txt')

def collect_names(names_number):
    names_list = ""

    while names_number > 0:
        user_name = input("What is your name?\n")
        names_list += user_name
        names_number -= 1    

    return names_list.splitlines()

final_names = collect_names(3)
# guest_book.write_text(final_names)
print(final_names)
        # names_list.append(user_name)
# guest_book.write_text(names_list).splitlines()
