from functools import reduce

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])

print(total)

def join_strings(liststrings):
    return " ".join(liststrings)

words = ["hello", "world"]

print(join_strings(words))