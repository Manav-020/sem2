
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            new_account = BankAccount(account_number, account_name, initial_balance)
            self.accounts[account_number] = new_account
            print("Account created successfully.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account number not found.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def display_all_accounts(self):
        for account in self.accounts.values():
            account.display_details()
            print()

def main():
    bank = Bank()

    while True:
        print("Banking System")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display Account Details")
        print("6. Display All Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, account_name, initial_balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.delete_account(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account number not found.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account number not found.")
        elif choice == "5":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.display_details()
            else:
                print("Account number not found.")
        elif choice == "6":
            bank.display_all_accounts()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
