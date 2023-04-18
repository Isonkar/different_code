'''сортировка через lambda
'''
x = [('Guido','van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]
x.sort(key=lambda name: len(' '.join(name)))
print(x)


#эквивалентно
x = [('Guido','van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]

def length(name):
  return len(' '.join(name))

name_lengths = [length(name) for name in x]
x.sort(key=length)
print(x)
