"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
#while loop
not_there = True
while not_there:
    print("Are we there yet?")
    print("Are we there yet?")
    print("Are we there yet?")
    arrived = input("Are we there yet? y/n   ")
    if arrived == "y" or arrived == "Y":
        not_there = False
    else:
        not_there = True

#for loop
for beer in range(99, 0, -1):
    print(f"{beer} bottles of beer on the wall,\n {beer} bottles of beer,\n take one down,\n pass it around,\n {beer - 1} bottles of beer on the wall!")