"""Напомним, что взаимно простыми называются числа, которые не имеют общих делителей кроме 1. Напишите программу, которая для каждого переданного числа находит список его взаимно простых.
Формат ввода

Задана последовательность чисел записанных через точку с запятой (;) и пробел.
Формат вывода

Список чисел с указанием взаимно простых ему среди переданных.
Все числа должны быть выведены в порядке возрастания без повторений.
Строки следует отформатировать по правилу:
число - взаимно простое 1, взаимно простое 2, ...
Если для числа не было найдено ни одного взаимно простого, то и выводить его не требуется.
Пример 1
Ввод

2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20

Вывод

2 - 3, 5, 7, 9, 11, 13, 15, 17, 19
3 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20
4 - 3, 5, 7, 9, 11, 13, 15, 17, 19
5 - 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19
6 - 5, 7, 11, 13, 17, 19
7 - 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20
8 - 3, 5, 7, 9, 11, 13, 15, 17, 19
9 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20
10 - 3, 7, 9, 11, 13, 17, 19
11 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20
12 - 5, 7, 11, 13, 17, 19
13 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20
14 - 3, 5, 9, 11, 13, 15, 17, 19
15 - 2, 4, 7, 8, 11, 13, 14, 16, 17, 19
16 - 3, 5, 7, 9, 11, 13, 15, 17, 19
17 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20
18 - 5, 7, 11, 13, 17, 19
19 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20
20 - 3, 7, 9, 11, 13, 17, 19

Пример 2
Ввод

7; 2; 2; 12; 14; 7; 2; 49

Вывод

2 - 7, 49
7 - 2, 12
12 - 7, 49
49 - 2, 12
"""

inp = sorted([int(i) for i in input().split('; ')])
my_dick = dict()
tmp = []
for count, number in enumerate(inp):
    for i in inp:
        tmp.clear()
        tmp.extend([number, i])
        while (ost := tmp[1] % tmp[0]) != 0:
            if ost != 1:
                tmp[0], tmp[1] = ost, tmp[0]
            else:
                try:
                    my_dick[number].add(str(i))
                except KeyError:
                    my_dick[number] = {str(i), }
                break

for i in my_dick:
    print(f'{i} - {", ".join(sorted(list(my_dick[i]), key=lambda x: int(x)))}')

     
         
