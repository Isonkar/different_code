'''Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepik.org/media/attachments/lesson/24472/sample0.html
https://stepik.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:
Yes

в задаче путаница с именем домена по этому необходимо заменять старый домен на новый!!!
'''

import requests
import re


# A = 'https://stepik.org/media/attachments/lesson/24472/sample0.html'
# B = 'https://stepik.org/media/attachments/lesson/24472/sample1.html'
A = input()
B = input()
all_links = []
links = []

links.extend(re.findall(r"<a href=\"(.*)\"", requests.get(A).text))

for link in links:
    all_links.extend(re.findall(r"<a href=\"(.*)\"", requests.get(link.replace('stepic.org', 'stepik.org')).text))

if B.replace('stepik.org', 'stepic.org') in all_links:
    print('Yes')
else:
    print('No')
    
    
# вариант два

import re
import requests

start_url = input()
end_url = input()

found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")
