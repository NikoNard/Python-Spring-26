"""
ASSIGNMENT 12B: SPRINT 5 - DATA PERSISTENCE
Project: Sandwich Order System V5
"""

ORDER_HISTORY = "order_history.txt"

#functions
def lookup():
    fname = input("Please enter first name: ").strip().title()
    lname = input("Please enter last name: ").strip().title()
    phone_number = input("Please enter phone number: ")
    #customer = fname + lname

    return fname, lname, phone_number

def read_menu():
    """ read_menu will import menu.txt and pull it into a list."""
    menus = {}
    try:
        # open and read file
        with open("menu.txt", 'r') as file:
            for line in file:
                parts_of_line = line.strip().split(';')
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

        # for x, y in menus.items():
        #     print(x, y)
        return menus
    except Exception as e:
        print(e)
        
def split_into_variables(menu_items):
    """break the menu file into separate variables"""

    sizes = menu_items.get("SIZES", "").split(',')
    prices = menu_items.get("PRICES", "").split(',')
    bread = menu_items.get("BREAD", "").split(',')
    protein = menu_items.get("PROTEIN", "").split(',')
    cheese = menu_items.get("CHEESE", "").split(',')
    topping = menu_items.get("TOPPINGS", "").split(',')
    sauce = menu_items.get("SAUCES", "").split(',')

    return sizes, prices, bread, protein, cheese, topping, sauce

def take_order(sizes, prices, bread, protein, cheese, topping, sauce):
    #collects sandwich order information: bread, protein, cheese, toppings, sauce
    num = 1

    for s in sizes:
        print(f"{num}.) {s} | Price ${prices[num-1]}")
        num += 1
    num = 1
    try:
        my_sizes = int(input("Please enter the number of your sandwich size:  "))-1
        if my_sizes < 0 or my_sizes >= len(sizes):
            print("Invalid entry, defaulting to 6 inch.")
            my_sizes = 0

    except Exception as e:
        print("Invalid input, defaulting to 6 inch.")
        my_sizes = 0
        print(e)

    for b in bread:
        print(f"{num}.)  {b}")
        num += 1
    num = 1
    try:
        my_bread = int(input("Please enter the number of your bread:  "))-1
        if my_bread < 0 or my_bread >= len(bread):
            print("Invalid entry, defaulting to white bread.")
            my_bread = 0
    except Exception as e:
        print("Invalid input, defaulting to white bread.")
        my_bread = 0
        print(e)

    for p in protein:
        print(f"{num}.)  {p}")
        num += 1
    num = 1
    try:
        my_protein = int(input("Please enter the number of your protein:  "))-1
        if my_protein < 0 or my_protein >= len(protein):
            print("Invalid entry, defaulting to turkey.")
            my_protein = 0
    except Exception as e:
        print("Invalid input, defaulting to turkey.")
        my_protein = 0
        print(e)

    for c in cheese:
        print(f"{num}.)  {c}")
        num += 1
    num = 1
    try:
        my_cheese = int(input("Please enter the number of your cheese:  "))-1
        if my_cheese < 0 or my_cheese >= len(cheese):
            print("Invalid entry, defaulting to american.")
            my_cheese = 0
    except Exception as e:
        print("Invalid input, defaulting to american.")
        my_cheese = 0
        print(e)

    for t in topping:
        print(f"{num}.)  {t}")
        num += 1
    num = 1
    try:
        my_topping = int(input("Please enter the number of your topping:  "))-1
        if my_topping < 0 or my_topping >= len(topping):
            print("Invalid entry, defaulting to lettuce.")
            my_topping = 0
    except Exception as e:
        print("Invalid input, defaulting to lettuce.")
        my_topping = 0
        print(e)

    for s in sauce:
        print(f"{num}.)  {s}")
        num += 1
    num = 1
    try:
        my_sauce = int(input("Please enter the number of your sauce:  "))-1
        if my_sauce < 0 or my_sauce >= len(sauce):
            print("Invalid entry, defaulting to mayo.")
            my_sauce = 0
    except Exception as e:
        print("Invalid input, defaulting to mayo.")
        my_sauce =  0
        print(e)

    return (sizes[my_sizes], bread[my_bread], protein[my_protein],
            cheese[my_cheese], topping[my_topping],
            sauce[my_sauce])

    
def preview_order(order):
    (sizes, bread, protein, cheese, topping, sauce) = order

    print("\n--- ORDER PREVIEW ---")
    print(f"Sizes: {sizes}")
    print(f"Bread: {bread}")
    print(f"Protein: {protein}")
    print(f"Cheese: {cheese}")
    print(f"Topping: {topping}")
    print(f"Sauce: {sauce}")

def calculate_total(order, prices, sizes):
    selected_size = order[0]
    total = 0
    num = 0
    for s in sizes:
        if s == selected_size:
            total = float(prices[num])
        num += 1

    print(f"\nTotal: ${total:.2f}")
    return total

def edit_order(sizes, prices, bread, protein, cheese, topping, sauce):
    print("\nEditing order")
    return take_order(sizes, prices, bread, protein, cheese, topping, sauce)

def delete_order():
    print("\nOrder has been canceled.")

def save_data_and_ticket(fname, lname, phone_number, order, total):
    (sizes, bread, protein, cheese, topping, sauce) = order

    # Save to file
    with open(ORDER_HISTORY, "a") as file:
        file.write("ORDER:\n")
        file.write(f"Name: {fname} {lname}\n")
        file.write(f"Phone: {phone_number}\n")
        file.write(f"sizes: {sizes}\n")
        file.write(f"Bread: {bread}\n")
        file.write(f"Protein: {protein}\n")
        file.write(f"Cheese: {cheese}\n")
        file.write(f"Topping: {topping}\n")
        file.write(f"Sauce: {sauce}\n")
        file.write(f"Total: ${total:.2f}\n\n")

    # Print ticket
    print("\nFINAL TICKET")
    print(f"Customer: {fname} {lname}")
    print(f"Phone: {phone_number}")
    print(f"Sizes: {sizes}")
    print(f"Bread: {bread}")
    print(f"Protein: {protein}")
    print(f"Cheese: {cheese}")
    print(f"Topping: {topping}")
    print(f"Sauce: {sauce}")
    print(f"Total: ${total:.2f}")
    print("Order saved successfully.")

def main():

    #1 Customer info and lookup
    fname, lname, phone_number = lookup()
    menu_items = read_menu()
    sizes, prices, bread, protein, cheese, topping, sauce, = split_into_variables(menu_items)

    #2 Taking order
    order = take_order(sizes, prices, bread, protein, cheese, topping, sauce)

    #3 Preview order
    preview_order(order)

    #4 Calculating total
    total = calculate_total(order, prices, sizes)

    #5 Confirm Order
    print("(C) Confirm Order")
    print("(E) Edit Order")
    print("(D) Delete Order")

    choice = input("Select an option: ").upper().strip()

    if choice == "E":
        order = edit_order(sizes, prices, bread, protein, cheese, topping, sauce)
        preview_order(order)
        total = calculate_total(order, prices, sizes)

    elif choice == "D":
        delete_order()
        return
    else:
        #6 Save order and print ticket
        save_data_and_ticket(fname, lname, phone_number, order, total)

main()