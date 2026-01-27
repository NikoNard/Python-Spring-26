"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f).
-----------------------------------------------------------------------
"""

#convert input

monthly_income = float(input("How much is your monthly income?  "))
rent = float(input("Amount spend on rent?  "))
car_payment = float(input("Amount spend on car payment?  "))
groceries = float(input("Amount spend on groceries?  "))
phone_bill = float(input("Amount spend on phone bill?  "))
utilities = float(input("Amount spend on utilities?  "))

# Equation

total_expenses = rent + car_payment + groceries + phone_bill + utilities
remaining_balance = monthly_income - total_expenses
percent = total_expenses / monthly_income 


# Display

print(f"You recieve {monthly_income: ,.2f}.")
print(f"You spent {total_expenses: ,.2f} a month.")
print(f"You have {remaining_balance: ,.2f} left.")
print(f"You spent {percent: .1%} of your income.") #used the AI to format the percentage correctly
