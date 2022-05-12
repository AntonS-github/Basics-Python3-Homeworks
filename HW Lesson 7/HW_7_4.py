'''4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.'''


import os
import stat
result_dict = {}
count_0 = 0
count_100 = 0
count_1000 = 0
count_10000 = 0
for root, dirs, files in os.walk('my_project'):
    for file in files:
        full_f_path = os.path.join(root, file)
        if os.path.getsize(full_f_path) == 0:
            count_0 += 1
        elif os.path.getsize(full_f_path) > 0 and os.path.getsize(full_f_path) <= 100:
            count_100 += 1
        elif os.path.getsize(full_f_path) > 100 and os.path.getsize(full_f_path) <= 1000:
            count_1000 += 1
        elif os.path.getsize(full_f_path) > 1000 and os.path.getsize(full_f_path) <= 10000:
            count_10000 += 1
result_dict = {'0': count_0,
               '100': count_100,
                '1000': count_1000,
                '10000': count_10000}
print(result_dict)
