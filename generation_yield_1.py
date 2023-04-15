''' генераторы, код в коментариях и код с генератором делают одно и тоже'''

from random import random

#
# class RandomIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration


def random_generation(k):
    for i in range(k):
        yield random()


gen = random_generation(3)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
