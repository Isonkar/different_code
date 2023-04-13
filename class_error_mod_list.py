'''Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.
В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение 
NonPositiveError и число не добавлялось, а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
Примечание:
Положительными считаются числа, строго большие нуля.'''


class PositiveList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x)
        else:
            raise NonPositiveError


class NonPositiveError(Exception):
    pass
  
  
  #вариант второй с функцией super()
    
    
  # создаем новый класс ошибки NonPositiveError
class NonPositiveError(Exception):
    pass             # ставим pass т.к. этот класс просто обертка для нашей выдуманной ошибки
                     # создаем новый класс листа, в который можем добавлять только положительные числа
                     # наследуем от существующего класса list
class PositiveList(list):

    def append(self, pos_number):         # переопределям метод append, когда вызываем PositiveList.append(x),
                                          # сработает именно он, а не list.append
        if pos_number > 0:                # делаем проверку полученного числа
            super().append(pos_number)    # если pos_number больше нуля, то вызываем обычный append листа с помощью super()
        else:                             # если мы не прошли проверку
            raise NonPositiveError(pos_number, "is less than 0!") # выбрасываем наше исключение с помощью raise

            
            
            
            
