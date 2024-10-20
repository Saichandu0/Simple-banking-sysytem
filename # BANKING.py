# Dictionary to store account details
accounts = {}

# Function to get valid input from user, includes "back" option
def get_valid_input(prompt, valid_range=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return 'back'
        try:
            user_input = int(user_input)
            if valid_range and user_input not in valid_range:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to create a new account
def create_account():
    while True:
        name = input("Enter a unique account name (or type 'back' to return): ").strip().lower()
        if name == 'back':
            return
        if name in accounts:
            print("Account name already exists. Please choose another name.")
        elif not name:
            print("Account name cannot be empty.")
        else:
            accounts[name] = 0  # Here we initialize balance to 0 for the user.
            print(f"Account '{name}' has been created successfully.")
            break

# Function to deposit money
def deposit_money():
    while True:
        name = input("Enter account name to deposit money (or type 'back' to return): ").strip().lower()
        if name.lower() == 'back':
            return
        if name in accounts:
            while True:
                amount = get_valid_input("Enter amount to deposit: ")
                if amount == 'back':
                    return
                if amount > 0:
                    accounts[name] += amount
                    print(f"₹{amount} has been deposited successfully. Current balance: ₹{accounts[name]}")
                    break
                else:
                    print("Deposit amount must be positive.")
            break
        else:
            print("Account not found. Please enter a valid account name.")

# Function to withdraw money
def withdraw_money():
    while True:
        name = input("Enter account name to withdraw money (or type 'back' to return): ").strip().lower()
        if name.lower() == 'back':
            return
        if name in accounts:
            print(f"Current balance: ₹{accounts[name]}")
            while True:
                amount = get_valid_input("Enter amount to withdraw: ")
                if amount == 'back':
                    return
                if amount > 0 and amount <= accounts[name]:
                    accounts[name] -= amount
                    print(f"₹{amount} has been withdrawn successfully. Current balance: ₹{accounts[name]}")
                    break
                elif amount > accounts[name]:
                    print("Insufficient funds.")
                else:
                    print("Withdrawal amount must be positive.")
            break
        else:
            print("Account not found. Please enter a valid account name.")

# Function to view balance
def view_balance():
    while True:
        name = input("Enter account name to view balance (or type 'back' to return): ").strip().lower()
        if name.lower() == 'back':
            return
        if name in accounts:
            print(f"Account balance for '{name}': ₹{accounts[name]}")
            break
        else:
            print("Account not found. Please enter a valid account name.")

# Function to delete an account
def delete_account():
    while True:
        name = input("Enter account name to delete (or type 'back' to return): ").strip().lower()
        if name.lower() == 'back':
            return
        if name in accounts:
            print(f"Account Name: {name}, Balance: ₹{accounts[name]}")
            confirmation = input("Are you sure you want to delete this account? (yes/no): ").lower()
            if confirmation == 'yes':
                del accounts[name]
                print(f"Account '{name}' has been deleted.")
                break
            elif confirmation == 'no':
                print("Account deletion has been canceled.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Account not found. Please enter a valid account name.")

# Function to display the main menu
def main_menu():
    print("Hello! Welcome to the Simple Banking System.")
    while True:
        print("\n--- Menu ---")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View balance")
        print("5. Delete account")
        print("6. Exit")

        choice = input("Choose an option (or type 'back' to return to menu): ").strip().lower()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            view_balance()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to run the program
def main():
    main_menu()
if __name__ == "__main__":
    main()
