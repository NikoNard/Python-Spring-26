"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS - Madlibs
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

#Three Blind Mice

print("\n\n\nThree Blind Mice")
print("        by: Agatha Christe")

#Variables
animal = input("Plural animal:   ")
verbA = input ("Random verb:   ")
nounA = input ("Random occupation:   ")
nounB = input ("Random noun:    ")
verbB = input ("Random verb:   ")

#Output
print(f"Three blind {animal}. Three blind {animal}")
print(f"\nSee how they {verbA}. See how they {verbA}")
print(f"\nThey all ran after the {nounA}'s wife")
print(f"\nWho cut off their tails with a {nounB}")
print(f"\nDid you ever {verbB} such a sight in your life")
print(f"\nAs three blind {animal}")