from abc import ABC,abstractclassmethod
class Human(ABC):
    @abstractclassmethod
    def gender(self):
        pass
class Male(Human):
    def gender(self):
        print("Male...")
class Female(Human):
    def gender(self):
        print("Female...")
x=Male()
x.gender()
