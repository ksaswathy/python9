class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("welcome to inheritance")
    
class dog(animal):
    def speak(self):
        print("says woof!!!!!!!!!",self.name)
class cat(animal):
    def speak(self):
        print("says meow!!!!!!!!!!",self.name)
d=dog("puppy")
d.speak()
c=cat("rubby")
c.speak()