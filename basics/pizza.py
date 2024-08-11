def make_pizza(size, *toppings):
    print(f"\nMaking a {size} pizza whith the following topings:\n")

    for topping in toppings:
        print(f"- {topping}")

