"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
from random import randint


def com1(in_dict):  # Решение 1 O(n log n)
    res = {}  # O(1)
    d = in_dict.copy()  # O(n)
    res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])[-3:]}  # O(n log n)
    return res  # O(1)


def comp2(in_dict):  # Решение 2 O(n)
    res = {}  # O(1)
    d = in_dict.copy()  # O(n)
    while len(res) < 3:  # O(1)
        m = None  # O(1)
        for key, val in d.items():  # O(n)
            if m is None:  # O(1)
                m = key  # O(1)
            if val > d[m]:  # O(1)
                m = key  # O(1)
        res[m] = d.pop(m)  # O(1)
    return res  # O(1)


"""
Вывод: 2-е решение comp2 лучшее, потому что при увеличении количества компаний сложность
алгоритма возрастает линейно, а не квадратично , как в первом варианте.
"""


companies = {f'company_{n}': yp for n, yp in enumerate([randint(-1000, 100000000) for i in range(100)])}
print(comp1(companies))
print(comp2(companies))