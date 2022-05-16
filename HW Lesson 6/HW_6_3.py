'''3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи'''


import json
import sys
from itertools import zip_longest
parced_hobby_info = []
parced_user_info = []
users_dict = {}
list_dicts = []
with open('users.csv', 'r', encoding='utf-8') as user_file:
    user_info = user_file.readlines()
    for line1 in user_info:
        line1 = line1.replace('\n', '').replace(',',' ')
        parced_user_info.append(line1)
with open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
    hobby_info = hobby_file.readlines()
    for line2 in hobby_info:
        line2 = line2.replace('\n', '')
        parced_hobby_info.append(line2)
#print(parced_user_info, parced_hobby_info)
    if len(parced_hobby_info) <= len(parced_user_info):
        for i in parced_user_info:
            users_dict = dict(zip_longest(parced_user_info, parced_hobby_info, fillvalue = 'None'))
    else:
        print('Exit')
        sys.exit(1)
with open('final_file.json', 'w') as ff:
    json.dump(users_dict, ff)
with open('final_file.json', 'r') as ff:
    final_file_read = json.load(ff)
print(final_file_read)
    
