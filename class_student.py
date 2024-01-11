class student:
    def __init__(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
    def display(self):
        print("student name is :",self.name, ",student phone is :",self.phone, ",student address is :",self.address)
#object creation
p1=student("thara",1122334455,"killimangalam")
#function calling using object
p1.display()
