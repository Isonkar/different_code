''' сортировка по последнему элементу, используя функционал библиотек operator и functools
'''
import operator
from functools import partial

x = [('Guido', 'van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]
sort_by_last = partial(list.sort, key=operator.itemgetter(-1))
print(x) # 1
sort_by_last(x) # данную функцию можно применять к любой коллекции(которую можно отсротировать, сортировка по последнему элементу)
print(x) # 1

# 1 -> [('Guido', 'van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]
# 2 -> [('John', 'Backus'), ('Haskell', 'Curry'), ('Guido', 'van', 'Rossum')]
