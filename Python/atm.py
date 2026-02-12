"""
Match Case ATM assignment
"""

balance = 1000

while True:
#menu
    print("1.  Balance")
    print("2.  Deposit")
    print("3.  Withdrawl")
    print("4.  Transfer")
    print("5.  Exit")
#input
    try:
        choice = int(input("Please enter the number of your choice:  "))
    except:
        print("Please enter a valid number 1-5")
        continue
    
    match choice:
        case 1:
            print(f"Your current total balance is ${balance:,.2f}")
        case 2:
            try:
                deposit = float(input("Please enter the amount you would like to deposit (0.00)  "))
            except:
                print("Please enter a valid number.")
                continue
            if deposit > 0:
                print(f"Succesfully deposited ${deposit:,.2f} ")
                balance += deposit
                print(f"New balance is ${balance:,.2f}")
            else:
                print("Please enter a positive number.")
        case 3:
            withdrawl = float(input("How much would you like to withdrawl? (0.00)   "))
            if withdrawl < 0:
                print("Invalid")
            else:
                if withdrawl > balance:
                    print("Insufficent funds")
                else:
                    print(f"Succesfully withdrew ${withdrawl:,.2f} ")
                    balance -= withdrawl
                    print(f"Balance remaining is ${balance:,.2f}")
        case 4:
            transfer = float(input("Please enter the amount you would like to transfer (0.00)  "))
            if transfer < 0:
                print("Invalid")
            else:
                if transfer > balance:
                 print("Insufficent funds")
                else:
                    print(f"Succesfully transfered ${transfer:,.2f} ")
                    balance -= transfer
                    print(f"Balance remaining is ${balance:,.2f}")
        case 5:
            print("Goodbye")
            break
        case _:
            print("Invalid Selection")
