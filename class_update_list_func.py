'''дополняем стандарнытй метод append объекта list т.о., 
      что после добавления элента выводится сообщение о том +- элемент + сам элемент'''


class MyList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x)
            print ('добавлено положительное число', x)
        elif x < 0:
            list.append(self, x)
            print ('добавлено отрицательное число', x)

test = MyList()
test.append(7)
