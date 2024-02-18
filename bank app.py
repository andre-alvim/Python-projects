# Account details
acc_details = ['lebleu@msn.com', 1234, 325428]

print("Welcome to our app")

while True:  # Main loop to keep the program running
    # Email details
    while True:
        email = input("please enter your email ")

        if email == acc_details[0]:
            print("Thank you.")
            break
        else:
            print("Invalid email.")

    # Password details
    while True:
        pin = input("please enter your PIN ")

        if pin == str(acc_details[1]):
            print("PIN accepted")
            break
        else:
            print("Incorrect PIN. Please try again")

    # Option of actions to perform
    while True:
        print("Welcome to your account")

        print("""
        1. to check your current balance
        2. to transfer funds
        3. to deposit an amount of money
        """)

        choice_action = int(input("What would you like to do? Please select a number "))

        if choice_action == 1:
            print(f"Your balance is £{acc_details[2]}")
        elif choice_action == 2:
            fund_transfer = int(input("How much do you want to transfer? "))
            while acc_details[2] < fund_transfer:
                print("Insufficient funds, please enter another amount.")
                fund_transfer = int(input("How much do you want to transfer? "))
            acc_details[2] -= fund_transfer
            print(f"£{fund_transfer} transferred successfully.")
        elif choice_action == 3:
            while True:
                try:
                    deposit_money = int(input("How much would you like to deposit? "))
                    break
                except ValueError:
                    print("Invalid entry. Please enter a valid amount.")
            acc_details[2] += deposit_money
            print(f"£{deposit_money} deposited successfully.")
        else:
            print("Incorrect option!")

        anything_else = input("Can we help you with anything else? (Yes/No)").capitalize()
        if anything_else != "Yes":
            print("Goodbye")
            break  # Break out of the inner loop if the user doesn't want further assistance

    # Check if the user wants to continue using the app
    continue_app = input("Would you like to continue using the app? (Yes/No)").capitalize()
    if continue_app != "Yes":
        print("Goodbye")
        break  # Break out of the outer loop if the user doesn't want to continue


        
        