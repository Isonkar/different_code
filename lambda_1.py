''' xs - последовательность чисел (сисок)
    выводим фильтрованную последовательность (только четные - реализовано через лямбду)
'''
xs = (int(i) for i in input().split())

evens = list(filter(lambda x: x % 2 == 0, xs))
print(evens)
