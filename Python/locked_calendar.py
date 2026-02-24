"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

#Constant tuple
MONTHS = ("January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December")

for month in MONTHS:
    print(month)

print("\nAttempt of modification toward tuple.")

#Shield to prevent program from crashing 
try:
    #Since the tuple is locked and immutable, this will trigger a TypeError
    MONTHS[2] = "Sarch"
except TypeError:
    print("\nError: this tuple is a constant and immutable")

