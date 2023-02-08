"""
Часто приходится обновлять данные.

Создайте программу, которая обновляет JSON файл.
Формат ввода

Пользователь вводит имя файла.
Затем вводятся строки вида ключ == значение.
Формат вывода

В заданный пользователем файл следует записать обновленный JSON.
Пример
Ввод

# Пользовательский ввод:
data.json
one == один
two == два
three == три

# Содержимое файла data.json
{
    "one": 1,
    "three": 2
}

Вывод

# Содержимое файла data.json
{
    "one": "один",
    "three": "три",
    "two": "два"
}
"""

import json
from sys import stdin
imp = [line.rstrip('\n').split('==') for line in stdin]
try:
    file_name = imp[0]
    with open(file_name[0], encoding="UTF-8") as file_in:
        records = json.load(file_in)
except FileNotFoundError:
    pass

for items in imp[1:]:
    records[items[0].strip(' ')] = items[1].strip(' ')

with open(file_name[0], "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)
