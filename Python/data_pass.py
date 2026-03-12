# """
# demo
# """

# def greeting(name):
#     print(f"Welcome to intro programming, {name}")

#     #return status

# def main():
#     identification = input("What is your name:   ")
#     greeting(identification)
#     identification = "Quinn"
#     # print(name) would not work, out of scope

# main()
"""
📚 ADD-100: Intro to Python | Demo: The Professional Order System
"""

# GLOBAL CONSTANTS (The Pantry)
MILKS = ("Oat", "Soy", "2%")
SYRUPS = ("Vanilla", "Caramel", "Simple Syrup")

def get_base_price(size):
    # Determine price based on size
    if size == "Small":
        return 1.00
    elif size == "Medium":
        return 1.50
    else:
        return 2.00

def brew_coffee(size, milk, syrup, pumps):
    # This function handles the final visual display
    print("\n--- Brewing Order ---")
    print(f"Size: {size}")
    print(f"Base: Coffee with {milk} milk.")
    print(f"Flavor: {syrup} ({pumps} pumps).")

def main():
    print("Welcome to Quacken Coffee Station")
    
    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_milk = input("Select Milk: ")
    choice_syrup = input("Select Syrup: ")
    
    try:
        packets = int(input("How many syrup pumps? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1.")
        packets = 1
    
    # Store the result from the return statement
    cost = get_base_price(choice_size)
    
    # Call the brew function
    brew_coffee(choice_size, choice_milk, choice_syrup, packets)
    
    print(f"Total Bill: ${cost:.2f}")

# Run the system
main()