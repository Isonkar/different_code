''' пример работы функции filter(), первый аргумент которой функция по которой производится логический отбор, 
второй аргумент - итерируемый объект'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def func_filter(num):

    if num % 2 == 0:
        return True
    else:
        return False


our_filter = filter(func_filter, a)
print(list(our_filter))
