# формируем датафрейм


import pandas as pd

data = {'apples': [3, 2, 0, 1],
        'oranges': [0, 3, 7, 2]
       }
purchases = pd.DataFrame(data, index=['Женя', 'Катя', 'Юля', 'Маша'])
print(purchases)

'''
      apples  oranges
Женя       3        0
Катя       2        3
Юля        0        7
Маша       1        2
'''

print(purchases)
print()
print(purchases.loc['Женя'])   # выводит данные по значению
'''
apples     3
oranges    0
Name: Женя, dtype: int64
'''
