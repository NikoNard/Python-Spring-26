"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

def read_menu():
    """ read_menu will import menu.txt and pull it into a list. We can then
        break down the list into the specific variables and
        dictionaries that we need. """
    menus = {}

    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(';')
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

        return menus
    except FileNotFoundError:
        print("Error, file not found")
    except Exception as e:
        print(e)


def split_into_variables(menu_items):
    """break the menu file into separate variables"""

    sizes = menu_items.get("SIZES")
    bread = menu_items.get("BREAD")
    protein = menu_items.get("PROTEIN")
    cheese = menu_items.get("CHEESE")

    return sizes, bread, protein, cheese

def print_menu(sizes, bread, protein, cheese):
    """Will print each menu"""
    print("\n MENU ")
    print(f"Sizes: {sizes}")
    print(f"Bread: {bread}")
    print(f"Protein: {protein}")
    print(f"Cheese: {cheese}")


def main():
    """organize program logic"""
    menu_items = read_menu()
    sizes, bread, protein, cheese = split_into_variables(menu_items)

    print_menu(sizes, bread, protein, cheese)


main()