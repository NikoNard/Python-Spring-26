"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [1/29/26]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""
#Buffet
print("This will determine your price for the buffet.")

#input 
age = int(input("How old are you?  "))

#dollar amount
amount_1 = 0.00
amount_2 = age * 1 
amount_3 = 16.95
amount_4 = 12.95

#pricing condition
if age < 1:
    print(f"${amount_1:,.2f}")
elif age < 12:
    print(f"${amount_2:,.2f}")
elif age < 65:
    print(f"${amount_3:,.2f}")
else: 
    print(f"${amount_4:,.2f}")
