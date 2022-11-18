
class Account:
    def __init__(self, account_name, account_balance):
        self.account_name = "John"
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient Balance")
            return False

    def get_balance(self):
        print("Account Balance: " + str(self.account_balance))

    def get_name(self):
        print("Account name: " + str(self.account_name))