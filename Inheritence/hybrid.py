class Mom:
    def character():
        print("So Soft..")
class Dad:
    def character():
        print("So Terror..")
class Grandpa:
    def character():
        print("He is a Gentle Man..")
class Son(Mom,Dad):
    def character():
        print(" I'm So kind...")
class GrandSon(Son,Grandpa):
    def character():
        print("So Naughty...")
me=GrandSon
me.character()