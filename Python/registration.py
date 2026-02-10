"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""
#name
first_name = ""
while len(first_name) == 0:
     first_name = input("What is your legal first name?  ")

last_name = ""
while len(last_name) == 0:
     last_name = input("What is your legal last name?  ")

#chaperone
chaperone = ""
while chaperone != "Y" and chaperone != "N":
    chaperone = input("Would you like to chaperone?   ").upper()

#phone number
phone_number = ""
while len(phone_number) == 0:
     phone_number = input("What is your phone number?  ")

#ticket count
tickets = 0
while tickets <= 0:
    try:
        tickets = int(input("How many tickets would you like?  "))
        if tickets <= 0:
            print("Tickets must be greater than 0.")
    except:
        print("Please enter a valid ticket count.")
#Output
print(f"Registration is complete for {first_name} {last_name}.")
print(f"Chaperone? {chaperone}")
print(f"Phone number {phone_number}")
print(f"Tickets {tickets}")