"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: The Sandwich System
"""

#constants
MENU_FILE = "menu.txt"
ORDER_HISTORY = "order_history.txt"

PRICES = {"6 inch": 5.00, "12 inch": 8.00}
BREAD = ("White", "Wheat", "Italian", "Multigrain", "Sourdough")
PROTEIN = ("Turkey", "Ham", "Pepperoni", "Chicken", "Steak", "None")
CHEESE = ("American", "Swiss", "Cheddar", "Provolone", "None")
TOPPINGS = ("Lettuce", "Tomato", "Onion", "Pickles", "None")
SAUCES = ("Mayo", "Mustard", "Ranch", "None")

def lookup():
    fname = input("Please enter first name: ")
    lname = input("Please enter last name: ")
    phone_number = input("Please enter phone number: ")
    customer = fname + lname

    return fname, lname, phone_number

def take_order():
    #collects sandwich order information: bread, protein, cheese, toppings, sauce
    num = 1

    for size, price in PRICES.items():
        print(f"{num}.) Size: {size} | Price ${price}")
        num += 1
    num = 1
    try:
        my_size = int(input("Please enter the number of your sandwich size:  "))
    except Exception as e:
        print({e})

    for bread in BREAD:
        print(f"{num}.)  {bread}")
        num += 1
    num = 1
    try:
        my_bread = int(input("Please enter the number of your bread:  "))
    except Exception as e:
        print({e})

    for protein in PROTEIN:
        print(f"{num}.)  {protein}")
        num += 1
    num = 1
    try:
        my_protein = int(input("Please enter the number of your protein:  "))
    except Exception as e:
        print({e})

    for cheese in CHEESE:
        print(f"{num}.)  {cheese}")
        num += 1
    num = 1
    try:
        my_cheese = int(input("Please enter the number of your cheese:  "))
    except Exception as e:
        print({e})

    for topping in TOPPINGS:
        print(f"{num}.)  {topping}")
        num += 1
    num = 1
    try:
        my_topping = int(input("Please enter the number of your topping:  "))
    except Exception as e:
        print({e})

    for sauce in SAUCES:
        print(f"{num}.)  {sauce}")
        num += 1
    num = 1
    try:
        my_sauce = int(input("Please enter the number of your sauce:  "))
    except Exception as e:
        print({e})

    return my_size, my_bread, my_protein, my_cheese, my_topping, my_sauce

    
def preview_order():
    #previews order info for confirmation
    pass

def calculate_total():
    #calculates the total price using the menu.txt file
    pass

def edit_order():
    #allows the user to change their order
    pass

def delete_order():
    #cancels the current order
    pass

def save_data_and_ticket():
    #saves the current order info to order_history.txt file and prints the final ticket
    pass

def main():

    #1 Customer info and lookup
    fname, lname, phone_number = lookup()

    #2 Taking order
    order = take_order()

    #3 Preview order
    preview_order(order)

    #4 Calculating total
    total = calculate_total(order)

    #5 Confirm Order
    print("(C) Confirm Order")
    print("(E) Edit Order")
    print("(D) Delete Order")

    choice = input("Select an option: ").upper().strip()

    if choice == "E":
        edit_order()
        preview_order()
        total = calculate_total()

    elif choice == "D":
        delete_order()
        return
    else:
        #6 Save order and print ticket
        save_data_and_ticket()

main()