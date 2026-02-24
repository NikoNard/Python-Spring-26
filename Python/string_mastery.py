"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: [YOUR NAME HERE]
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR ðŸŽ¸ ---
instrument = "Acoustic Guitar"
print(len(instrument))
print(instrument[0], instrument[-1])
print(min(instrument))
print(max(instrument))

# --- TASK 2: THE CLEANUP CREW ðŸ§µ ---
messy_input = "   vOLUME_knob_11   "
print(f"{messy_input.strip()}")
print(f"{messy_input.strip().upper()}")
print(f"{messy_input.strip().upper().replace("_", " ")}")


# --- TASK 3: THE VALIDATOR ðŸ” ---
serial_number = "90210"
if serial_number.isdigit():
    print("Valid Serial")
else:
    print("Invalid Serial")

# --- TASK 4: THE DUCK BRIDGE ðŸ¦†ðŸŽµ ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("\n--- Singing the Duck Song! ---")
for char in name_string:
    current_name = " ".join(duck_letters)

    print("There was a teacher who had a duck and Ducky was his Name-o")
    print((f"({current_name}) \n") *3)
    print("and Ducky was his Name-o!\n")

    duck_letters[count] = "🦆"
    count += 1

final_name = " ".join(duck_letters)
print("There was a teacher who had a duck and Ducky was his Name-o")
print(f"({final_name}) \n" * 3)
print("and Ducky was his Name-o!")