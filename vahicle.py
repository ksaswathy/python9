class Vahicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print("welcome to vahicle world")

class Car(Vahicle):
    def display(self):
        print("car brand is :",self.brand,"car model is :",self.model)

class Motorcycle(Vahicle):
    def power(self):
        print("motorcycle brand is :",self.brand,"motorcycle model is :",self.model)   

c=Car("Audi","2023A6")
c.display()

m=Motorcycle("x pulse","200 4v")
m.power()