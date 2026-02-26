"""
demo
"""

#Testing data
# errors = True
# while errors: 
#     try: 
#         name = input("Please enter your first and last name:  ").title()
#         first_name, last_name = name.split(" ")
#         print(name)
#         print(first_name)
#         print(last_name)
#         print(f"{first_name[0]}{last_name[0]}")
#         errors = False
#     except ValueError as e:
#         print(f"You have a value error {e}")
#     except Exception as e:
#         print(f"This raised an exception: {e}")
    


"""
in demo
"""

# my_string = "Dr. Meri Kasprak"
# if "Dr." in my_string:
#     print("Yes, individual has a doctorate")
# else:
#     print("No individual has no doctorate")

# days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

"""
Time list string bridge
"""
import time
# 1. Start with an empty bar string
empty_bar = "----------"
bar_list = list(empty_bar) # Breakdown to ["-", "-", ...]

print("Initiating Rocket Launch Sequence...")

for i in range(len(bar_list)):
    # Update the specific index in the LIST
    bar_list[i] = "🚀"

    # JOIN back to a STRING to display
    current_status = "".join(bar_list)
    print(f"Status: [{current_status}]")
    time.sleep(1)

print("Liftoff!")