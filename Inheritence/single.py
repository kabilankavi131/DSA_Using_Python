class Bank:
    balance=0
    def __init__(self,name):
        print("Welcome to our bank..")
        self.name=name
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def get_balance(self):
        print("Current Bank Balance : ",self.balance)
class IOB(Bank):
    def get_balance(self):
        print("Current IOB Bank Balance : ",self.balance)
user=IOB("Kabilan K")
user.deposit(20000)
user.get_balance()
user.withdraw(10000)
user.get_balance()