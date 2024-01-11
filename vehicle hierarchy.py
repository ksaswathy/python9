class vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print(self.model,"started")
    def stop(self):
        print(self.model,"stopped")

class car(vehicle):
    def display(self,num):
        self.num=num
        print("make year of car :",self.make,"model of car :",self.model,"\n","number of doors of car:",self.number)
    
class motorcycle(vehicle):
    def display(self,num):
        self.num=num
        print("make year of motorcycle :",self.make,"\n","model of motorcycle :",self.model)

c=car(1999,"audi 2023A6")
c.start()
c.display()
c.stop()

m=motorcycle(2020,"x pulse 200 4v")
c.start()
c.display()
c.stop()



