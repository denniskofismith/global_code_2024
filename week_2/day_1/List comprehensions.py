##   List comprehensions

numbers1 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

postnumbs = [numbs for numbs in numbers1 if numbs > 0]

print(postnumbs)

numbers2 = [12, 54, 33, 67, 24, 89, 11, 24, 47]

evennumbs = [numbs for numbs in numbers2 if numbs % 2 == 0]

print(evennumbs)


words = ["hello", "my", "name", "is", "Sam"]

uppwords = [(word.upper(),len(word)) for word in words]

print(uppwords)
  