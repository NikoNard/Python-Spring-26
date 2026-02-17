"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
#seat list
seats = list(range(1,21))

while len(seats) > 0:
    print("Available seats:", seats)

    #input
    try:
        choice = int(input("Enter seat number to purchase (0 to exit): "))
        if choice == 0:
            print("Goodbye.")
            break
        if choice in seats:
            seats.remove(choice)
            print(f"Seat {choice} has been successfully purchased.")
        else:
            print("Sorry, that seat is already taken or does not exist.")
    except:
        print("Invalid input.")

if len(seats) == 0:
    print("All seats are sold out.")