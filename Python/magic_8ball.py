"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

#Responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later", "It is likely", "It is not likely", "Possibly", "Improbable" )

print("Welcome to the Digital Oracle!")
while True:
    question = input("Type your question(type quit to exit): ")

    #quit
    if "quit" in question.lower():
        print("Goodbye")
        break

    #8ball response
    answer = random.choice(RESPONSES)
    print(answer)