# """
# demo
# """
# def options():
#     #give options to order, print labels, see history
#     print("options")

# def menu():
#     #present menu options
#     print("menu")

# def order_system():
#     print("Order system")
#     #take orders from customer
#     #read in past orders and display
#     #call save function
#     menu()
#     name = input("Please enter your name:  ")
#     #read file to look for last order
#     read_orders()

#     save_orders()

# def read_orders():
#     # reads stored orders
#     print("read orders")

# def save_orders():
#     #write to file
#     print("Save Orders")

# def print_labels():
#     #print on avery 2 by 3 inch labels
#     print("print labels")

# def calculate_cost():
#     #calculate cost (read in order)
#     print("calculate cost")

# def main():
#     options()
#     order_system()
#     calculate_cost()
#     print_labels()

# main()
"""
 1. Demonstrate functions
 2. Interface design (menus/ passing)
"""
COFFEE = ("Espresso", "Americano", "Latte", "Cappuccino",
          "Macchiato", "Mocha", "Flat White", "TEA", "COCOA")

PRICES = {
    "Small": 3.00,
    "Medium": 4.00,
    "Large": 5.00,
    "Extra Large": 6.00
}

MILKS = ("Soy", "Oat", "Whole", "Coconut", "2%", "None")

FLAVORS = ("Vanilla", "Caramel", "Hazelnut", "Mocha",
           "Peppermint", "Pumpkin Spice", "Sugar Free Vanilla")

SHOTS = ("Normal: 6", "Light: 3", "Heavy, 9")


def lookup():
    fname = input("Please Enter First Name: ")
    lname = input("Please Enter your Last Name: ")
    extension = input("Please enter your extension: ")
    emp_num = input("please enter your employee number: ")

    return fname, lname, extension, emp_num


def ordering_system():
    # give options to order, print labels, see history
    num = 1
    my_coffee = 3

    for coffee in COFFEE:
        print(f"{num}.)  {coffee}")
        num += 1

    num = 1
    for size, price in PRICES.items():
        print(f"Size: {size:12}.) | Price ${price}")
        num += 1

    num = 1
    for milk in MILKS:
        print(f"{num}.)  {milk}")
        num += 1

    try:
        my_coffee = int(
            input("Please enter the number of your drink order:  "))

        my_size = int(
            input("Please enter the number of your drink size:  "))

        print(f"Your oder is:  ")

        return my_coffee, my_size

    except Exception as e:
        print(f"drink type {e}")


def read_orders():
    # reads stored orders
    # new text file at beginning of each month
    # can be used to deduct coffee from check
    # can see previous orders and select to order again or make new order
    pass


def save_orders():
    # Write to file
    print("Save Orders")


def print_labels():
    # print on avery 2 by 3 inch labels
    print("Print labels")


def calculate_cost():
    # Calculate cost (read in order)
    print("Calculate cost")


def main():
    first, last, extension, emp_num = lookup()
    coffee, size, milk, flavor, shots = ordering_system()
    calculate_cost()
    print_labels()


main()
