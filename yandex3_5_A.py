"""
Напишите программу, которая находит сумму всех чисел введённых пользователем.
Формат ввода

Вводятся строки чисел.
Формат вывода

Одно число — сумма всех чисел в потоке ввода.
"""

from sys import stdin
from itertools import accumulate

resp = []
for line in stdin:
    resp.extend([int(i) for i in line.rstrip('\n').split()])
print(sum(resp))

