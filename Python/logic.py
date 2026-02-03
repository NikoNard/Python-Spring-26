"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

#input
math_test = int(input("What was your score on your math test"  ))
history_test = int(input("What was your score on your history test"  ))

#both > 0
if math_test > 0 and history_test > 0:
    print("You got at least one question right on both tests.")
else:
    print("You didn't get at least one question right on both tests.")

#both > 100
if math_test > 100 and history_test > 100:
    print("You scored higher than a 100 on both tests.")
else:
    print("You did not score higher than a 100 on both tests.")

#either even
if math_test % 2 == 0 or history_test % 2 == 0:
    print("At least one of your test scores were even.")
else:
    print("Neither of your test scores were even.")

#either < 100
if math_test < 100 or history_test < 100:
    print("You scored less than 100 on one of your tests.")
else:
    print("You scored at least a 100 on both tests.")

#not equal
if math_test != history_test:
    print("You have different scores on both tests.")
else:
    print("You scored the same on both tests.")

#not zero
if math_test != 0 and history_test != 0:
    print("Neither test score was 0.")
else:
    print("At least one of the test scores were 0.")

#math test categorization
if math_test > 0:
    print("The math score is positive.")
elif math_test < 0:
    print("The math score is negative.")
else:
    print("The math score is 0.")