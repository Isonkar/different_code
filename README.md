# different_code
содержит разные задачи, из разных курсов, решение которых оставляю для более детального разбора

 15/04/2023 почитать yield - https://habr.com/ru/articles/132554/

Заметки:

Генераторы
 - {ord(x) for x in 'spaam'}    # генерируем set {112, 115, 109, 97}
 - {x:ord(x) for x in 'spaam'}  # генерируем dictionary {'s': 115, 'm': 109, 'p': 112, 'a': 97}

Если список содержит последовательно пары key value, то так можно преобразовать в словарь:
 - d = ['Dota', 'sucks', 'Python', 'rules', 'Saperavi', 'depends']
 - dictus = {d[x]: d[x+1] for x in range(0, len(d), 2)}
