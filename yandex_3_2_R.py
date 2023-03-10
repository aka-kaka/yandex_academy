"""На пиратской карте отмечено N точек, в которых зарыты сокровища. Каждая точка задана координатами (xixi​, yiyi​). Координаты указаны в километрах. Команда Капитана Крюка хочет составить маршрут, чтобы собрать как можно больше кладов. Однако есть ограничение: для любых двух соседних точек маршрута (xixi​, yiyi​) и (xjxj​, yjyj​) координаты xixi​ и xjxj​ могут различаться только последней цифрой, как и координаты yiyi​ и yjyj​ тоже могут различаться только последней цифрой. Например, после точки (15, 10) они могут отправиться в точку (18, 16), а вот из точки (14, 68) в точку (19, 71) пройти уже не получится, ведь 68 и 71 различаются не только последней цифрой. Из точки (5, 12) в точку (13, 14) попасть тоже нельзя, так как числа 5 и 13 отличаются в разряде десятков. По заданным координатам определите, какое максимальное количество точек сможет добавить в свой маршрут Капитан Крюк.
Формат ввода

В первой строке указано число NN (1≤N≤1051≤N≤105) — количество точек, отмеченных на карте сокровищ. В следующих N строках содержатся пары координат: xixi​ и yiyi​ — координаты ii-ой точки. Координаты — целые числа не меньше нуля и не больше 109109. Гарантируется, что совпадающих точек в списке нет.
Формат вывода

Выведите одно число — максимальное количество точек, которое Капитан Крюк сможет посетить по маршруту, построенному по описанным правилам.
Пример
Ввод

9
10 18
17 15
25 21
0 21
1 16
25 29
24 24
8 26
10 20

Вывод

3
"""

my_dick = {}
for _ in range(int(input())):
    index = [(int(i) // 10) for i in input().split()]
    try:
        my_dick[index[0], index[1]] += 1
    except KeyError: 
        my_dick[index[0], index[1]] = 1
print(max(set(my_dick.values())))
     
         
