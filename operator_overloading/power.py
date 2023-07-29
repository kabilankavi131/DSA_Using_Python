class Employee:
    def __init__(self,amount):
        self.balance=amount
    def __pow__(a,b):
        return a.balance**b.balance
emp1=Employee(8)
emp2=Employee(2)
print(emp1**emp2)