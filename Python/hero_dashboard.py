"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS
OFFICE_NAME = "The Office"
TAX_RATE = 0.05

def process_expenses(base_price, item_desc):

    tax = base_price * TAX_RATE
    total = base_price + tax
    item_desc = item_desc.title()

    return total, item_desc

def main():
    try:
        item = input("Enter item name: ").strip()
        user_price = float(input("Enter order price: "))
    except ValueError:
        print("Invalid input. Defaulting to 1.00")
        user_price = 1.00
        item = "unknown"
    except Exception as e:
        print({e})

    # UNPACKING the two returned values
    final_cost, item_txt = process_expenses(
        base_price=user_price, item_desc=item)

    print(f"\n{OFFICE_NAME} Receipt: ${final_cost:.2f}")
    print(f"Order: {item_txt}")

main()