class Employee:
    count=0
    @staticmethod
    def no_of_employees():
        return Employee.count
    def __init__(self):
        Employee.count+=1
y=Employee()
z=Employee()
a=Employee()
x=Employee()
print(Employee.no_of_employees())