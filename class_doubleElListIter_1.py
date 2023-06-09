'''выводим парами элементы списка, список должен быть четной длины(контроль условия четности не реализован)'''

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


for pair in MyList([1, 2, 4, 5, 6, 7]):
    print(pair)

