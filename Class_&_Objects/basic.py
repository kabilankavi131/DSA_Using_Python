class Employee():
    name=''
    age=0
    Company=''
    Salary=0
    def increment(__init__,bonus):
        __init__.Salary+=bonus
    def __init__(self):
        print("Welcome Guys")
emp1=Employee()
setattr(emp1,'name','Kabilan K')
setattr(emp1,'age',19)
setattr(emp1,'Company','Aroopa')
setattr(emp1,'Salary',30000)
emp1.increment(1000)
print(getattr(emp1,'name'))
print(getattr(emp1,'Hike','Not Found'))
delattr(emp1,'age')
print(emp1.__dict__)