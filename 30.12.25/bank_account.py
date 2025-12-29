# Bank Account Management System in Python

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
            print(f"New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
            print(f"New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")
    
    def display(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ${self.balance}")

# Main
if __name__ == "__main__":
    account = BankAccount("123456", "John Doe", 1000)
    account.display()
    account.deposit(500)
    account.withdraw(300)
    account.display()
