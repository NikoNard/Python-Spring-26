"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""
#constant
TOPPINGS = ("Pepperoni", "Mushrooms", "Bacon", "Sausage")


def make_pizza(customer, size, topping, is_delivery=False, number=1):
    print(f"Customer: {customer}")
    print(f"Size: {size}")  
    print(f"Topping: {topping}")

    if is_delivery:
        print("Delivery")
    else:
        print("Pickup")
    print(f"Number of pizzas: {number}")
def main():
    
    try:
        customer = input("\nEnter your name: ").title().strip()
        size = input("Enter pizza size (Small/Medium/Large): ").title().strip()
        print(f"Available toppings: {TOPPINGS}")
        topping = input("Choose a topping: ").title().strip()
        delivery = input("Is this for delivery? (Yes/No): ").title().strip()
        if delivery == "Yes":
            is_delivery = True
        else:
            is_delivery = False
        number = int(input("How many pizzas would you like? "))
    except ValueError:
        print("Invalid input, defaulting to 1 pizza.")
        number = 1
    print("\nFinal Order Ticket:")
    make_pizza(customer=customer, size=size, topping=topping, is_delivery=is_delivery, number=number)

main()
