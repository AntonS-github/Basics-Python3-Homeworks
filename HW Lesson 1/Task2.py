'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
  этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.)
'''


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    number = 0
    sum = 0
    total_sum = 0
    odd_cubed = 0

    sum_figures = 0
    list = []
    sum_digits = []
    for i in range(1, 1001):
        if i % 2 != 0:
            odd_cubed = i ** 3
            i += 1
        while odd_cubed > 0:
            sum_figures += odd_cubed % 10
            odd_cubed = odd_cubed // 10
            sum_digits.append(sum_figures)
            sum = 0
            for sum in sum_digits:  # проверка деления на 7
                if sum % 7 == 0:
                    total_sum += odd_cubed  # суммирование кубов, сумма цифр которых делится на 7
    # print(f'Список сумм цифр числе списка: {sum_digits}')
    print(f'Сумма тех чисел, сумма цифр которых делится нацело на 7: {total_sum}')
    return 1  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    sum_17 = 0
    total_sum_17 = 0
    odd_cubed_17 = 0
    sum_figures_17 = 17
    sum_digits_17 = []
    for i in range(1, 1001):
        if i % 2 != 0:
            odd_cubed_17 = i ** 3 + 17
            i += 1
        while odd_cubed_17 > 0:
            sum_figures_17 += odd_cubed_17 % 10
            odd_cubed_17 = odd_cubed_17 // 10
            sum_digits_17.append(sum_figures_17)
            sum_17 = 0
            for sum_17 in sum_digits_17:  # проверка деления на 7
                if sum_17 % 7 == 0:
                    total_sum_17 += odd_cubed_17
    print(f'Сумма тех чисел (с добавлением 17), сумма цифр которых делится нацело на 7: {total_sum_17}')
    return 1  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)