class Employee():
    name=''
    age=0
    Company=''
    Salary=0
    def increment(__init__,bonus):
        __init__.Salary+=bonus
    def __init__(self):
        print("Welcome Guys")
    def hi(self):
        print("Hi Employees...")
class Manager(Employee):
    @property
    def hi(self):
        print("Hi Managers...")

emp1=Employee()
m1=Manager()
m1.hi