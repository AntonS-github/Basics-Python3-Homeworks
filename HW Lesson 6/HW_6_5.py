'''5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.'''

import sys
csv_users = sys.argv[1]
csv_hobby = sys.argv[2]
csv_output = sys.argv[3]
with open(csv_users, 'r+', encoding='utf-8') as file_1, \
	open(csv_hobby, 'r+', encoding='utf-8') as file_2, \
	open(csv_output, 'w+', encoding = 'utf-8') as result:
	line_1 = file_1.read().splitlines()
	line_2 = file_2.read().splitlines()
	for i in range(len(line_1)):
		result.writelines(line_1[i] + ': ' + line_2[i] + '\n')