class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("my name is :",self.name, ",my age is :",self.age)
#object creation
p1=person("thara",5)
#function calling using object
p1.display()