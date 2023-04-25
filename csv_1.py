'''Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
Файл с данными:
Crimes.csv
'''
import csv

lst_crimes=[]
with open('Crimes.csv') as data:
    reader = csv.reader(data)
    for row in reader:
        if '2015' in row[2]:
            lst_crimes.append(row[5])

print(max(lst_crimes, key=lst_crimes.count))


#вариант

import csv

with open("Crimes.csv") as fi:
    reader = csv.reader(fi)
    next(reader)
    crime_cnt = dict()
    for row in reader:
        year = row[2][6:10]
        if year == "2015":
            crime_type = row[5]
            if crime_type not in crime_cnt:
                crime_cnt[crime_type] = 0
            crime_cnt[crime_type] += 1

a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
a.sort(key=lambda x: -x[0])

print(a[0][1])


#вариант три(через pandas) почитать углубленно

import pandas as pd
doc = pd.read_csv("Crimes.csv")
print(doc.groupby(['Primary Type']).count())
