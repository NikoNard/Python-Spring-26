"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: The Sandwich System
"""

#constants
MENU_FILE = "menu.txt"
ORDER_HISTORY = "order_history.txt"


def get_customer_info():
    #asks for customer name
    pass

def take_order():
    #collects sandwich order information: bread, protein, cheese, toppings, sauce, quantity
    pass

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

    #1 Customer info
    customer = get_customer_info()

    #2 Taking order
    order = take_order()

    #3 Preview order
    preview_order()

    #4 Calculating total
    total = calculate_total()

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
    else:
        #6 Save order and print ticket
        save_data_and_ticket()

main()