from abc import ABC,abstractmethod

#define abstract class

class Shape(ABC):
    #abstract mothods
    def area(self):
        print("area of the shape")

    def peremeter(self):
        print("peremeter of shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    
    def peremeter(self):
        return 2*3.14*self.radius
    
class Sqaure(Shape):
    def __init__(self,side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length*self.side_length
    
    def peremeter(self):
        return 4*self.side_length
    
#object creation 

c=Circle(3)
s=Sqaure(4)

print("circle area",c.area())
print("circle peremeter",c.peremeter())

print("square area",s.area())
print("square peremeter",s.peremeter())

    

        