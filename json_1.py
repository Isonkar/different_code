'''
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.
Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass
class B(A, C):
    pass
class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.
Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
'''
import json

# data = json.loads(input())  # ввод входящих данных
# data = [{"name": "A", "parents": []},
#         {"name": "B", "parents": ["A", "C"]},
#         {"name": "C", "parents": ["A"]}
#         ]
data = json.loads(input())
with_children = {element['name']: [] for element in data}
print(with_children)

for eli in data:
    for elc in with_children:
        if elc in eli['parents']:
            with_children[elc].append(eli['name'])
print(with_children)

for element in with_children:
    with_children[element] = set(with_children[element])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))

    
#вариант два
import json

data = json.loads(input())
children = dict()

for cls in data:
    for par in cls["parents"]:
        if par not in children:
            children[par] = []
        children[par].append(cls["name"])

def dfs(v, used):
    size = 1
    used.add(v)
    if v not in children:
        return size

    for child in children[v]:
        if child not in used:
            size += dfs(child, used)

    return size

ans = []

for cls in data:
    ans.append((cls["name"], dfs(cls["name"], set())))

for i in sorted(ans):
    print(i[0], ":", i[1])
    
#вариант три
import json
data = json.loads(input(''))
def find(a):
    for j in data:
        if a['name'] in j['parents']:
            ans[i['name']].add(j['name'])
            find(j)
    
ans = {}
for i in data:
    ans[i['name']] = {1}# i- словарь из списка data
    find(i)
for i in sorted(ans):
    print(i, ':', len(ans[i]))
