"""
Напишите программу, которая для заданного файла вычисляет следующие параметры:

    количество всех чисел;
    количество положительных чисел;
    минимальное число;
    максимальное число;
    сумма всех чисел;
    среднее арифметическое всех чисел с точностью до двух знаков после запятой.

Формат ввода

Пользователь вводит два имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
Формат вывода

Выведите статистику во второй файл в формате JSON.

Ключи значений задайте соответственно:

    count — количество всех чисел;
    _positivecount — количество положительных чисел;
    min — минимальное число;
    max — максимальное число;
    sum — сумма всех чисел;
    average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.

Пример
Ввод

# Пользовательский ввод:
numbers.txt
statistics.json

# Содержимое файла numbers.txt
1 2 3 4 5
-5 -4 -3 -2 -1
10 20
20 10

Вывод

# Содержимое файла statistics.json
{
    "count": 14,
    "positive_count": 9,
    "min": -5,
    "max": 20,
    "sum": 60,
    "average": 4.29
}
"""

from itertools import chain
import json
from sys import stdin


def get_lines_from_file(file_name: str):
    '''
    inp
    '''
    try:
        with open(file_name, 'r', encoding='utf-8') as file_in:
            return iter([
                item.strip('\n ').split(' ')
                for item in file_in.readlines()
            ])
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    my_dick = {
        'count': 0,
        'positive_count': 0,
        'min': int(),
        'max': int(),
        'sum': 0,
        'average': 0,
    }
    ipo = [line.rstrip('\n').split(' ') for line in stdin]
    my_iter_tmp = get_lines_from_file(ipo[0][0])
    res_items = [int(i) for i in chain(*my_iter_tmp) if i != '']
    for items in res_items:
        my_dick['count'] += 1
        if int(items) > 0:
            my_dick['positive_count'] += 1
        my_dick['sum'] += items
    my_dick['min'] = min(res_items)
    my_dick['max'] = max(res_items)
    my_dick['average'] = round(
        my_dick['sum'] / my_dick['count'], 2
    ) if my_dick['count'] else 0
    if ipo[1][0]:
        with open(ipo[1][0], "w", encoding="utf-8") as file_out:
            json.dump(my_dick, file_out, indent=2)
