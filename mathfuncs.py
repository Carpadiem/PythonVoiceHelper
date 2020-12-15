import math


def plus(a=int(input()), b=int(input())):  # сложение
    result = a + b
    return result


def minus(c=int(input()), d=int(input())):  # Вычитание
    result = c - d
    return result


def divide(e=int(input()), r=int(input())):  # Деление
    result = e / r
    return result


def multiply(q=int(input()), z=int(input())):  # Умножение
    result = q * z
    return result


def root(g=int(input())):  # корень
    result = math.sqrt(g)
    return result


def opred_matrix():  # Определитель матрицы
    array = [
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())]
    ]

    answer = array[0][0] * array[1][1] * array[2][2] + array[2][0] * array[0][1] * array[1][2] + array[0][2] * array[1][
        0] * array[2][1] - array[2][0] * array[1][1] * array[0][2] - array[1][0] * array[0][1] * array[2][2] - array[2][
                 1] * array[1][2] * array[0][0]
    return answer


def plus_matrix():  # Сложение матриц
    array = [
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())]]
    array1 = [
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())],
        [int(input()), int(input()), int(input())]

    ]
    answer = [array[0][0] + array1[0][0], array[0][1] + array1[0][1], array[0][2] + array1[0][2]], [
        array[1][0] + array1[1][0], array[1][1] + array1[1][1], array[1][2] + array1[1][2]], [
                 array[2][0] + array1[2][0], array[2][1] + array1[2][1], array[2][2] + array1[2][2]]

    return answer


def len_circle():  # длина окружности
    red = int(input())
    ot = 2 * math.pi * red
    return ot


def v_sphere():  # обьем шара
    sha = int(input())
    ras = (4 / 3) * (math.pi * sha ** 3)
    return ras


def v_cube():  # обьем куба
    length = int(input())
    result = length ** 3
    return result


def v_pyramid():  # объем пирамиды
    height = int(input())  # высота
    s_base = int(input())  # площадь основания
    result = (1 / 3) * (height * s_base)
    return result


def s_circle():  # Площадь круга
    radius = int(input())  # радиус
    result = math.pi * radius
    return result


def s_squad():  # площадь прямоугольника
    length = int(input())
    width = int(input())
    result = length * width
    return result


def obj_trl():  # площадь треугольника
    base = int(input())  # основание
    height = int(input())  # высота
    result = (1 / 2) * base * height
    return result


arr_nums_words = [
    'ноль', 'один', 'два', 'три', 'четыре',
    'пять', 'шесть', 'семь', 'восемь', 'девять'
]

arr_nums_nums = [
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9
]


def translate(word):
    if len(word) == 1:
        for k in arr_nums_words:
            if word == arr_nums_words[k]:
                word = arr_nums_nums[k]
