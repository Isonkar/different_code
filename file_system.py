'''разбор методов билиотеки os, shutil
'''

import os
import os.path
import shutil

print(os.getcwd()) #какая папка является текущей
print(os.listdir('.idea')) #перечисляет все, что содержится в текущей папке

print(os.path.exists('general.py'))
print(os.path.exists('new_general.py'))
print(os.path.exists('venv'))

print(os.path.isfile('general.py'))
print(os.path.isdir('venv'))

print(os.path.abspath('general.py'))

# os.chdir('yaprakti')
# print(os.getcwd())

shutil.copy('dataout.txt', 'dataout2.txt')

for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)
