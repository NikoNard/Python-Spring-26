"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

def get_price(size):
    if size =="Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00


def blend(size, base, fruit, scoops):
    print("\n Order")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")

def main():
    print ("Welcome to the smoothie shop")

    choice_size = input("Size (Small, Medium, Large):   ").title().strip()
    choice_base = input("Select base:   ").title().strip()
    choice_fruit = input("Select fruit:  ").title().strip()

    try:
        scoops = int(input("How many scoops?   "))
    except ValueError:
        print("Invalid input, defaulting to 1 scoop.")
        scoops = 1
    cost = get_price(choice_size)
    blend(choice_size, choice_base, choice_fruit, scoops)
    print(f"Total: ${cost:.2f}")

main()