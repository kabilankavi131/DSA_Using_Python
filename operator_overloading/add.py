class Employee:
    def __init__(self,amount):
        self.balance=amount
    def __add__(a,b):
        return a.balance+b.balance
emp1=Employee(10000)
emp2=Employee(20000)
print(emp1+emp2)