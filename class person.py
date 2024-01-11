class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print("name is :",self.name,"age is :",self.age)
    

class fam(person):
    def display(self,employee_id):
        print("employee_id is :",self.employee_id)
    def display(self,empid):
        self.empid=empid
        print("employee_id is:",self.empid,"employeename is :",self.name)

p2=fam("thara",5)
p2.display(101)

           
n=name("ajmal")
n.speak()
a=age("6")
a.speak()


        
    