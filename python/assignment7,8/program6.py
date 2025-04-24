class BankAccount:
    def __init__(self, acc_number, acc_holder, balance=0.0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount:.2f}. Updated balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount:.2f}. Remaining balance: {self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        return self.balance

    def display_details(self):
        print(f"Account Number: {self.acc_number}, Holder Name: {self.acc_holder}, Balance: {self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_number, acc_holder, initial_deposit=0.0):
        if acc_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[acc_number] = BankAccount(acc_number, acc_holder, initial_deposit)
            print("Account created.")

    def find_account(self, acc_number):
        return self.accounts.get(acc_number, None)

    def list_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            for account in self.accounts.values():
                account.display_details()

# User Interaction
def main():
    bank = Bank()
    while True:
        print("\nOptions:")
        print("1. Open Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. View Account Details")
        print("5. Show All Accounts")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            acc_num = input("Enter Account Number: ")
            name = input("Enter Account Holder's Name: ")
            initial_deposit = float(input("Initial Deposit Amount: "))
            bank.add_account(acc_num, name, initial_deposit)
        elif choice == "2":
            acc_num = input("Enter Account Number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = float(input("Enter Amount to Deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            acc_num = input("Enter Account Number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = float(input("Enter Withdrawal Amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            acc_num = input("Enter Account Number: ")
            account = bank.find_account(acc_num)
            if account:
                account.display_details()
            else:
                print("Account not found.")
        elif choice == "5":
            bank.list_accounts()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()