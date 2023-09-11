class Cricketer:
    def special_shot(self)->None:
        print("Normal Special shot...")
class Dhoni(Cricketer):
    def special_shot(self) -> None:
       print("Helicopter Shot....")
class Virat(Cricketer):
    def special_shot(self) -> None:
        print("Cover Drive Shot...")
def special_shot(Cricketer):
    Cricketer.special_shot()
v=Virat()
d=Dhoni()
special_shot(v)
special_shot(d)