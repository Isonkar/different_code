'''Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
Для лучшего понимания формата задачи, ознакомьтесь с примером.
'''

import os
import os.path


result_lst = []
with open('out.txt', 'w') as out:

    for current_dir, dirs, files in os.walk('main'):
        for file in files:
            if file.endswith('.py'):
                # if current_dir not in result_lst:
                result_lst.append(current_dir)
                break

    result_lst.sort()
    for path in result_lst:
        path = path.replace('\\', '/')
        out.write(path + '\n')

#вариант два (короткий)
import os

result = [cur_dir for cur_dir, dirs, files in os.walk("main") if any((fl.endswith(".py")
    for fl in files))]

with open("py_dirs.txt", "w") as w:
    w.write("\n".join(sorted(result)))
    
    
#вариант три
# Пример обхода иерархии самого zip файла без распаковывания!!! Оригинальное задание показалась мне нелогичноым
# зачем распаковывать весь архив лишь для того чтобы узнать есть в нём необходимые файлы или нет? 
# Логичнее сначала найти в архиве нужные файлы и только потом разпаковать только содержащие их папки!!! Код приведённый ниже как раз выполняет первую часть задачи.
# В модуле zipfile нету точного аналога os.walk, поэтому пришлось немного поколдовать чтобы не сохранять одни и те же имена папок по нескольку раз:

import zipfile, os

pydirs = list()

with zipfile.ZipFile('main.zip', 'r') as zip:
    for zip_path in zip.namelist():
        if  os.path.dirname(zip_path) not in pydirs and os.path.basename(zip_path).endswith('.py'):
            pydirs.append(os.path.dirname(zip_path))

print('\n'.join(sorted(pydirs)))
