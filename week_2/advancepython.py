
names = ["sam","john",'james']

koddy = map(len,names)

for names in names:
    print(len(names))

print(tuple(koddy))


def too_old(x): 
    turple_1 , tuple_2 = x
    return turple_1 + tuple_2 > 50

ages =[(22,5),(25,29),(34,56),(24,17)]


koddy = filter(too_old,ages)

print(list(koddy))

def acceptable_students(x):
    age = x['age']
    classes = x['class']

    return (age > 25) and (classes >= 2)

students = [{"age":30,"class": 2},{"age": 300,"class":1},{"age": 30,"class": 3}]



print(list(filter(acceptable_students,students)))

items = [1,2,3,4,5]

squares = map((lambda x: x**2), items)

print(list(squares))
