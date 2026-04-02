"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""
import datetime

def get_bug_info():
    
    file_name = input("Enter file name (or type 'Quit' to quit): ").lower().strip()

    if file_name == "quit":
        return "Quit"

    description = input("Enter bug description: ")
    priority = input("Enter priority (Low/Medium/High): ")

    bug_data = {
        "file_name": file_name,
        "description": description,
        "priority": priority
    }

    return bug_data
def save_to_file(timestamp_str, bug_data):
    with open("bug_log.txt", "a") as file:
        file.write("Bug Entry\n")
        file.write(f"Time: {timestamp_str}\n")
        file.write(f"File: {bug_data['file_name']}\n")
        file.write(f"Description: {bug_data['description']}\n")
        file.write(f"Priority: {bug_data['priority']}\n\n")

def main():
    while True:
        bug = get_bug_info()

        if bug == "Quit":
            print("Exiting bug tracker")
            break

        current_time = datetime.datetime.now()

        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        save_to_file(timestamp_str, bug)

        print("Bug logged successfully")

main()