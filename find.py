'''Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.
Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:

abababa
abababa
abababa

Sample Input 1:
abababa
aba
'''

s, t = input(), input()

cnt = 0
while s.find(t) != -1:
    cnt += 1
    s = s[s.find(t) + 1:]
print(cnt)
