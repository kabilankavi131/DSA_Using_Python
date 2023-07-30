class Employee():
    def __init__(self,fname,lname,company="gmail") -> None:
        self.lname=lname
        self.fname=fname
        self.company=company
    @property
    def email(self):
        return f"{self.fname}{self.lname}@{self.company.lower()}.com"
    @email.setter
    def email(self,mail):
        self.fname,self.lname=mail.split("@")[0].split("n")
emp1=Employee("Kabilan","kavi","Aroopa")
print(emp1.email)
emp1.email="kabilankavi131@gmail.com"
print(emp1.email)