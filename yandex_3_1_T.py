"""Потренируемся в ОПН дальше. Операции, которые выполняются с одним значением, называются унарными, с двумя — бинарными, с тремя — тернарными. Давайте улучшим наш калькулятор, добавив поддержку следующих операций:

    бинарные:
        + (сложение),
        - (вычитание),
        * (умножение),
        / (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);
    унарные:
        ~ (унарный минус — меняет знак),
        ! (факториал),
        # (клонирование — вернуть в стек значение дважды);
    тернарные:
        @ (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).

Формат ввода

Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций. Вместе они составляют корректное выражение в обратной польской нотации, не содержащее деления на ноль и взятия факториала от отрицательного числа.
Формат вывода

Выводится одно целое число — результат вычисления выражения.
Примечание

В первом примере стек по мере прочтения строки выглядит так:

    7
    7 1
    7 1 10
    7 1 10 100
    7 1 10 100 100
    7 1 10 10000
    7 10 10000 1
    7 10 9999
    7 10009
    10016
    -10016

Пример 1
Ввод

7 1 10 100 # * @ - + + ~

Вывод

-10016

Пример 2
Ввод

10 15 - 7 *

Вывод

-35
"""

def my_sum(*args):
    return [args[1] + args[0], ]


def my_subs(*args):
    return [args[1] - args[0], ]


def my_mult(*args):
    return [args[1] * args[0], ]


def my_div(*args):
    return [args[1] // args[0], ]


def my_un_min(*args):
    return [-args[0], ]


def my_factorial(*args):
    fact = 1
    for i in range(args[0]):
        fact *= (i + 1)
    return [fact, ]


def my_dbl_last(*args):
    return [args[0], args[0]]


def my_ret_tree(*args):
    return [args[1], args[0], args[2]]


TMP_DICT = {
    '+': [my_sum, 2],
    '-': [my_subs, 2],
    '*': [my_mult, 2],
    '/': [my_div, 2],
    '~': [my_un_min, 1],
    '!': [my_factorial, 1], 
    '#': [my_dbl_last, 1],
    '@': [my_ret_tree, 3],
}
if __name__ == '__main__':
    inp = list(reversed(input().split()))
    res = []
    while len(inp) != 0:
        try:
            tmp = inp.pop()
            res.append(int(tmp))
            continue
        except ValueError:
            my_func, count = TMP_DICT[tmp]
            res.extend(my_func(*[res.pop() for _ in range(count)]))
    else:
        print(res[0])

     
         
