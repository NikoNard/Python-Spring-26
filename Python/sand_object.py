"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project.
[ ] 3. Use __init__ to set variable.
[ ] 4. Write Setters and Getters.
[ ] 5. Write a summary function that prints or returns all properties
[ ] 6. Instantiate two objects and call their 'intro' method.
-----------------------------------------------------------------------
"""

class Sandwich:
    def __init__(self, bread, protein, cheese, toppings, sauce):
        self.__bread = bread
        self.__protein = protein
        self.__cheese = cheese
        self.__toppings = toppings
        self.__sauce = sauce

#setters
    def set_bread(self, bread):
        self.__bread = bread

    def set_protein(self, protein):
        self.__protein = protein

    def set_cheese(self, cheese):
        self.__cheese = cheese

    def set_toppings(self, toppings):
        self.__toppings = toppings

    def set_sauce(self, sauce):
        self.__sauce = sauce
#getters
    def get_bread(self):
        return self.__bread

    def get_protein(self):
        return self.__protein

    def get_cheese(self):
        return self.__cheese

    def get_toppings(self):
        return self.__toppings

    def get_sauce(self):
        return self.__sauce
#summary
    def summary(self):
        print(f"Sandwich has {self.__bread} bread, {self.__protein} protein, {self.__cheese} cheese, {self.__toppings} toppings, and {self.__sauce} sauce.")

    def intro(self):
        print("Sandwich order:")
        self.summary()

sandwich1 = Sandwich("Wheat", "Turkey", "Swiss", "Lettuce", "Mayo")
sandwich2 = Sandwich("White", "Ham", "Cheddar", "Pickles", "Mustard")

sandwich1.intro()
sandwich2.intro()