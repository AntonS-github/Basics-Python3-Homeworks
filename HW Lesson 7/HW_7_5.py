'''
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]), например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт.
'''

import os
import stat
result_dict = {}
count_0 = 0
count_100 = 0
count_1000 = 0
count_10000 = 0
ending_0 = []
ending_100 = []
ending_1000 = []
ending_10000 = []
for root, dirs, files in os.walk('my_project'):
    for file in files:
        full_f_path = os.path.join(root, file)
        if os.path.getsize(full_f_path) == 0:
            count_0 += 1
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext not in ending_0:
                ending_0.append(ext)
        elif os.path.getsize(full_f_path) > 0 and os.path.getsize(full_f_path) <= 100:
            count_100 += 1
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext not in ending_100:
                ending_100.append(ext)
        elif os.path.getsize(full_f_path) > 100 and os.path.getsize(full_f_path) <= 1000:
            count_1000 += 1
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext not in ending_1000:
                ending_1000.append(ext)
        elif os.path.getsize(full_f_path) > 1000 and os.path.getsize(full_f_path) <= 10000:
            count_10000 += 1
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext not in ending_10000:
                ending_10000.append(ext)
result_dict_5 = {'0': (count_0, ending_0),
               '100': (count_100, ending_100),
                '1000': (count_1000, ending_1000),                
                '10000': (count_10000, ending_10000)}
print(result_dict_5)