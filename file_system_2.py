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
