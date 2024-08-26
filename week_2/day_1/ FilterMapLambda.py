def is_even(x): return x % 2 == 0 

numbers = [1,56,234,87,4,76,24,69,90,135]

evenNumbs = filter(is_even,numbers)

print(list(evenNumbs))



def is_odd(x): return x % 2 != 0 

numbers = [1,56,234,87,4,76,24,69,90,135]

evenNumbs = filter(is_even,numbers)

evenNumbs = filter(is_odd,numbers)

print(list(evenNumbs))

###  LAMBDA 

evenlambdafunc = lambda x : x % 2 == 0

oddlambdafunc = lambda x : x % 2 != 0


print(evenlambdafunc(2))

print(evenlambdafunc(2))