'''разбор методов билиотеки os, shutil
'''

import os
import os.path
import shutil

print(os.getcwd()) #какая папка является текущей
print(os.listdir('.idea')) #перечисляет все, что содержится в текущей папке

print(os.path.exists('general.py'))
print(os.path.exists('new_general.py')) #возвращает булевое значение "есть ли этот файл"
print(os.path.exists('venv'))

print(os.path.isfile('general.py')) # проверка "это файл"
print(os.path.isdir('venv')) # проверка "это папка"

print(os.path.abspath('general.py')) # показывает абсолютный путь к файлу

# os.chdir('yaprakti') # смена директории
# print(os.getcwd())

shutil.copy('dataout.txt', 'dataout2.txt') #копирует первый файл во второй (т.е. создает копию первого)

for current_dir, dirs, files in os.walk('.'): #проходит все папки и подпапки и выводит current_dir, dirs, files
    print(current_dir, dirs, files)
