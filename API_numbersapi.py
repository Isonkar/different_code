import requests
import json


res_lst = []
with open('dataset_24476_3 (7).txt') as data:
    for line in data:
        number = line.strip()
        api_url = f"http://numbersapi.com/{number}/math?json=true"
        res = requests.get(api_url).json()
        if res['found']:
            res_lst.append('Interesting')
        else:
            res_lst.append('Boring')

    for el in res_lst:
        print(el)
        
        
#самое важное в программировании - читаемость 

import requests


with open('dataset.txt') as f:
    read = f.read().splitlines()

for x in read:
    res = requests.get(f'http://numbersapi.com/{x}/math?json=true')
    if res.json()['found'] == True:
        print('Interesting')
    else:
        print('Boring')
        
'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''
