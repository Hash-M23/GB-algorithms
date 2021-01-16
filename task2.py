"""
Задание 2.
Реализуйте два алгоритма.
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


def min_kv(lst):
    """
    Квадратичная сложность
    """
    for i in range(len(lst)):
        cnt = 0
        for j in range(len(lst)):
            if lst[i] <= lst[j]:
                cnt += 1
            else:
                break
        if cnt == len(lst):
            return lst[i]


def min_lin(lst):
    """
    Линейная сложность
    """
    min_e = lst[0]
    for elem in lst:
        if elem < min_e:
            min_e = elem
    return min_e


print(min_kv([6, 0, -1, 1, 27]))
print(min_lin([6, 0, -1, 1, 27]))