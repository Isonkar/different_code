""" Словарь в одну строку. Ключи - четные числа, значения их степень (2)"""

print({i: i * i for i in range(1, 20) if not i % 2})


""" Тоже самое но не в одну строку"""
res = {}
for i in range(1, 20):
    if i % 2 == 0:
        res.setdefault(i, i * i)
print(res)
