'''интересная библиотека операторов
'''

import operator as op

print(op.add(5, 6))  # сложение
print(op.mul(5, 6))  # умножение
print(op.contains([5, 6, 4, 7, 1], 4))  # есть ли элемент в последовательности - выводит бул

xx = [1, 2, 3]
f = op.itemgetter(1)  # f(x) -> x[1] выводит элемент с индексом 1
print(f(xx))

x = [('Guido', 'van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]
x.sort(key=op.itemgetter(-1))  # сортирует по фамилии -1 (крайний с права элемент)
print(x)
