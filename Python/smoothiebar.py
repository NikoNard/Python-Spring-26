"""
demo
"""
def options():
    #give options to order, print labels, see history
    print("options")

def menu():
    #present menu options
    print("menu")

def order_system():
    print("Order system")
    #take orders from customer
    #read in past orders and display
    #call save function
    menu()
    name = input("Please enter your name:  ")
    #read file to look for last order
    read_orders()

    save_orders()

def read_orders():
    # reads stored orders
    print("read orders")

def save_orders():
    #write to file
    print("Save Orders")

def print_labels():
    #print on avery 2 by 3 inch labels
    print("print labels")

def calculate_cost():
    #calculate cost (read in order)
    print("calculate cost")

def main():
    options()
    order_system()
    calculate_cost()
    print_labels()

main()