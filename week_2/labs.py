


# ###  LAMBDA 

# evenlambdafunc = lambda x : x % 2 == 0

# oddlambdafunc = lambda x : x % 2 != 0


# print(evenlambdafunc(2))

# print(evenlambdafunc(2))



####  COMBINATIONS

# def is_even(x): return x % 2 is not 0 

# numbers = [1,56,234,87,4,76,24,69,90,135]

# evenNumbs = filter(is_even,numbers)

# print(list(evenNumbs))



# ###  FOLD
# from functools import reduce

# total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])

# print(total)

# def join_strings(liststrings):
#     word = ""
#     for x in len(liststrings) :
#         word =  liststrings[x] + " "
#     return word
# stringg = ["Koddy","Smith","yaw","esi"]

# print(join_strings(stringg))




###   List comprehensions

# numbers1 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

# postnumbs = [numbs for numbs in numbers1 if numbs > 0]

# print(postnumbs)

# numbers2 = [12, 54, 33, 67, 24, 89, 11, 24, 47]

# evennumbs = [numbs for numbs in numbers2 if numbs % 2 == 0]

# print(evennumbs)


# words = ["hello", "my", "name", "is", "Sam"]

# uppwords = [(word.upper(),len(word)) for word in words]

# print(uppwords)
  

######  Modules

from conditionals import age


print(age())



#### CLASSES

# class Person :
#     def __init__(self,name=str,dob=int) :
#         self.name = name
#         self.dob = dob

#     def speak(self) :
#         print("Hello")

#     def walk(self) :
#         print("Walking Away")

#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return 2024 - self.dob
    
# class Students(Person):
#     def __init__(self,name=str,dob=int,course=list):
#         self.course = course
#         Person.__init__(self,name,dob)

#     def get_course(self):
#         return self.course
    
#     def speak(self):
#         print("I'm so tired!")

# koddy = Person("Koddy Smith",2002)

# print(koddy.get_age())
# print(koddy.get_name())
# koddy.speak()
# koddy.walk()


# studen1 = Students("Ansah",1990,["Math","Geography","physics","science"])

# studen1.walk()

# studen1.speak()

# print(studen1.get_age())
# print(studen1.get_course())

        






