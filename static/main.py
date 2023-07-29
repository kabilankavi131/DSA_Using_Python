class Employee:
    count=0
    @staticmethod
    def no_of_employees(self):
        self.count=1
        return self.count
    def __init__(self):
        self.no_of_employees()
x=Employee
y=Employee
z=Employee
a=Employee
print(Employee.no_of_employees())