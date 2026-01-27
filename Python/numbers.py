#Demo

#convert input

allowence = float(input("How much is your allowence?  "))
snacks = float(input("Amount spend on snacks?  "))
video_games = float(input("Spent on video games?  "))

# Equation
remaining = allowence - snacks - video_games
spent = snacks + video_games
percent = snacks/allowence
# Display

print(f"You recieve {allowence: ,.2f}.")
print(f"You spent {spent: ,.2f} a month.")
print(f"You have {remaining: ,.2f} left.")
print(f"You spent %{percent: ,.2f} on snacks.")