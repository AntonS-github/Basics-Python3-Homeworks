'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

def transform_string() -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    percent = list(range(1, 101))
    var1 = ' процент'
    var2 = ' процента'
    var3 = ' процентов'
    for item in percent:
        if item < 10 or item >= 21:
            if item % 10 == 1:
                print(item, var1)
            elif 1 < item % 10 <= 4:
                print(item, var2)
            else:
                print(item, var3)
        else:
            print(item, var3)
    return 'верните отформатированную строку'
print(transform_string())
'''
if __name__ == '__main__':
    for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
        print(transform_string(n))
'''