## CLASSES

class Person :
    def __init__(self,name=str,dob=int) :
        self.name = name
        self.dob = dob

    def speak(self) :
        print("Hello")

    def walk(self) :
        print("Walking Away")

    def get_name(self):
        return self.name
    
    def get_age(self):
        return 2024 - self.dob
    
class Students(Person):
    def __init__(self,name=str,dob=int,course=list):
        self.course = course
        Person.__init__(self,name,dob)

    def get_course(self):
        return self.course
    
    def speak(self):
        print("I'm so tired!")

koddy = Person("Koddy Smith",2002)

print(koddy.get_age())
print(koddy.get_name())
koddy.speak()
koddy.walk()


studen1 = Students("Ansah",1990,["Math","Geography","physics","science"])

studen1.walk()

studen1.speak()

print(studen1.get_age())
print(studen1.get_course())