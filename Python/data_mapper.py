"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""
#dictionary
"""
prompt: create a dictionary in python of the full NATO alphabet A-Z and include common punctuation as the same
"""
NATO_ALPHABET = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
    ".": ".",
    ",": ",",
    "?": "?",
    "!": "!",
    ":": ":",
    ";": ";",
    "-": "-",
    "_": "_",
    "(": "(",
    ")": ")",
    "\"": "\"",
    "'": "'",
    "/": "/",
    "\\": "\\",
    "@": "@",
    "#": "#",
    "$": "$",
    "%": "%",
    "&": "&",
    "*": "*",
    "+": "+",
    "=": "=",
    " ": " "
}
#input
word = input("Enter word to spell: ").upper()

#output
for letter in word:
    try:
        print(NATO_ALPHABET[letter])
    except:
        print(f"{letter} is not a valid letter in the NATO alphabet.")