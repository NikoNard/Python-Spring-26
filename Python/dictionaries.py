"""
demo
"""

# create dictionary
japanese_numbers = {
    "one": "ichi",
    "two": "ni",
    "three": "san",
    "four": "yon",
    "five": "go",
    "six": "roku",
    "seven": "nana",
    "eight": "hachi",
    "nine": "kyuu",
    "ten": "juu"
}

if "eleven" in japanese_numbers:
    print("found")
else:
    print("missing")

#lookup key
print(japanese_numbers["seven"])

# days in months

days_in_months = {
    "January": 30,
    "February": 28,
    "March": 31,
}
for key, value in days_in_months.items():
    print(f"{key}:{value}")
print("\n\n")

days_in_months["April"] = 30

for key, value in days_in_months.items():
    print(f"{key}:{value}")
print("\n\n")

#delete
days_in_months.pop("January")

for key, value in days_in_months.items():
    print(f"{key}:{value}")
print("\n\n")



"""
📚 ADD-100: Intro to Python | Demo: Resilient Lookup Schema
"""

# 1. Define the Schema
translator = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco"
}

word = input("Enter an English number (one-five): ").lower().strip()

# 2. Perform a Resilient Lookup
try:
    translation = translator[word]
    print(f"System Output: {translation}")
except KeyError:
    print(f"!! DATA INTEGRITY WARNING: '{word}' is not in our system.")

