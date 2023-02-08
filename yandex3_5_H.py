"""
Напишите программу, которая определяет, какие слова есть только в одном из файлов.
Формат ввода

Пользователь вводит три имени файлов.
Каждый из входных файлов содержит произвольное количество слов, разделённых пробелами и символами перевода строки.
Формат вывода

В третий файл выведите в алфавитном порядке без повторений список слов, которые есть только в одном из файлов.
Пример
Ввод

# Пользовательский ввод:
first.txt
second.txt
answer.txt

# Содержимое файла first.txt
кофе молоко
чай печенье
велосипед

# Содержимое файла second.txt
кофе велосипед
пряник жвачка весло

Вывод

# Содержимое файла answer.txt
весло
жвачка
молоко
печенье
пряник
чай

"""
from sys import stdin

inp = [line.rstrip('\n').split(' ') for line in stdin]
res = []
for file_name in inp:
    tmp = []
    try:
        with open(file_name[0], 'r', encoding='utf-8') as file_in:
            for i in file_in.readlines():
                tmp.extend(i.rstrip('\n').split())
    except FileNotFoundError:
        pass
    res.append(set(tmp))
diff1 = res[0].symmetric_difference(res[1])
diff2 = res[2].symmetric_difference(res[0].intersection(res[1]))
fin_res = sorted(diff1.difference(diff2))
with open(inp[-1][0], 'w', encoding='utf-8') as file_out:
    file_out.writelines('\n'.join(fin_res))
