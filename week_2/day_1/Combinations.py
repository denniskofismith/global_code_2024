def is_even(x): return x % 2 is not 0 

numbers = [1,56,234,87,4,76,24,69,90,135]

evenNumbs = filter(is_even,numbers)

print(list(evenNumbs))