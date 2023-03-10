"""
Формат ввода

В единственной строке записывается последовательность натуральных чисел, разделённых пробелами.
Формат вывода

Требуется вывести одно натуральное число — НОД всех данных чисел.
Примечание

Самый распространенный способ поиска НОД — Алгоритм Эвклида."""
"""
Ввод

102 39 768

Вывод

3

Ввод

12 42

Вывод

6
"""
def my_func(f_int: int(), sec_int: int()):

    sec_int, f_int = max(sec_int, f_int), min(sec_int, f_int)
    while (f_int % sec_int) != 0:
        f_int, sec_int = sec_int, f_int % sec_int
    return sec_int


if __name__ == "__main__":
    inp = sorted([int(i) for i in input().split()])
    res = my_func(inp.pop(), inp.pop())
    while len(inp) != 0:
        res = my_func(res, inp.pop())
    print(res)
         
