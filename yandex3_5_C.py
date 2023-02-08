"""
Как вы помните, когда вы комментируете свой код, перед его выполнением интерпретатор удаляет комментарии.
Напишите программу, которая выполняет данную функцию за интерпретатор.
Формат ввода

Вводятся строки программы.
Формат вывода

Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не нужно.
Пример 1
Ввод

# Моя первая супер-пупер программа
print("What is your name?") #  Как тебя зовут?
name = input() #  Сохраняем имя
print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы

Вывод

print("What is your name?")
name = input()
print(f"Hello, {name}!")

Пример 2
Ввод

# Мой первый цикл
for i in range(10): # Считаем до 10
    print(i) # выводим число

Вывод

for i in range(10):
    print(i)
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:02:43 2022

@author: oslik-bob
"""

from sys import stdin


def clip_string(list_string: str):
    '''
    return string
    '''
    return list_string.split('#')[0]


if __name__ == "__main__":

    res = []
    for lines in stdin:
        strings = clip_string(lines.rstrip('\n'))
        if strings:
            res.append(strings)
    print('\n'.join(res))

