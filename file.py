class BankAccount:
    def __init__(self, name): 
        self.int_rate = .01
        self.balance = 0
        self.name = name
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.name + "'s balance: $" +str(self.balance))
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    def transfer(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
        BankAccount 
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(self.name + "'s balance: " +str(self.balance))
        return self
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

jeremy = BankAccount("Jeremy")
jeremy.deposit(500).deposit(300).deposit(200).withdraw(500).yield_interest().display_account_info()
bob = BankAccount("bob")
bob.deposit(4000).deposit(4000).withdraw(2000).withdraw(2000).withdraw(2000).withdraw(1000).yield_interest().display_account_info()
