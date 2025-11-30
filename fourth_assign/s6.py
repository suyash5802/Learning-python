class Person:
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(self.name)

        if self.age is not None:
            print(self.age)
        if self.address is not None:
            print(self.address)
    




p1=Person("Suyash",23)
p1.display()

p2=Person("Suyash",23,"10/206")
p2.display()




