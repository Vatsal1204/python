class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter your name: ").strip()
        while True:
            try:
                initial_deposit = float(input("Enter initial deposit amount: "))
                if initial_deposit < 0:
                    raise ValueError("Initial deposit cannot be negative.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        self.accounts[name] = initial_deposit
        print("Account created successfully!")

    def deposit_funds(self):
        name = input("Enter account name: ").strip()
        if name not in self.accounts:
            print("Error: Account does not exist.")
            return
        while True:
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    raise ValueError("Deposit amount must be positive.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        self.accounts[name] += amount
        print(f"Deposit successful! Your new balance is: {self.accounts[name]}")

    def withdraw_funds(self):
        name = input("Enter account name: ").strip()
        if name not in self.accounts:
            print("Error: Account does not exist.")
            return
        while True:
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    raise ValueError("Withdrawal amount must be positive.")
                if amount > self.accounts[name]:
                    raise ValueError("Insufficient funds.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        self.accounts[name] -= amount
        print(f"Withdrawal successful! Your new balance is: {self.accounts[name]}")

    def check_balance(self):
        name = input("Enter account name: ").strip()
        if name not in self.accounts:
            print("Error: Account does not exist.")
            return
        print(f"Your current balance is: {self.accounts[name]}")

    def run(self):
        while True:
            print("\nWelcome to the Robust Banking System!")
            print("1. Create Account")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_funds()
            elif choice == "3":
                self.withdraw_funds()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                print("Thank you for using the Robust Banking System! Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    bank = BankingSystem()
    bank.run()
