"""
Формат ввода

Вводятся слова.
Формат вывода

Список слов-палиндромов в алфавитном порядке без повторений.
Примечание

При проверке слов не обращайте внимание на регистр.
Пример
Ввод

Анна Боря Вова
Я последняя буква алфавита
Дед строит шалаш
Шалаш был хорош
Дед слышит топот
Ара залетел в шалаш

Вывод

Анна
Ара
Дед
Шалаш
Я
в
топот
шалаш
"""

from sys import stdin
from itertools import chain

inp = [line.rstrip('\n').split(' ') for line in stdin]
res = set()
for item in chain(*inp):
    len_item = len(item)
    if len_item % 2 == 0:
        if (
            item[:int(len_item / 2)].lower() ==
            item[-1:int(len_item / 2) - 1:-1].lower()
        ):
            res.add(item)
    else:
        if (
            item[:int(len_item / 2)].lower() ==
            item[-1:int(len_item / 2):-1].lower()
        ):
            res.add(item)
for i in sorted(chain(res)):
    print(i)
