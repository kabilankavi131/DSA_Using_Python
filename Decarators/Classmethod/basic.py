class Employee:
    def __init__(self) :
        print("Welcome Employee..")
    @classmethod
    def year_of_experience(cls,a):
        return a
    
print(Employee.year_of_experience("Fresher..."))
