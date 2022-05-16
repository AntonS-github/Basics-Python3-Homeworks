'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


# делаем через реквесты, сплит и строковые методы. Для экономии ОЗУ юзаем readline. Collections - модуль для выявления спамера.

'''
from collections import Counter

spam_count = 0
with open('nginx_logs.txt', 'r') as logs:
	line_data = logs.readline()
	counter = 0
	result_list = []
	while line_data:
		line_data = line_data.replace('"', '')
		work_line = line_data.split()
		remote_addr = work_line[0]
		request_type = work_line[5]
		requested_resource = work_line[6]
		result = (remote_addr, request_type, requested_resource)
		result_list.append(result)
		line_data = logs.readline()
		counter += 1
spam_count = Counter(result_list).most_common(3)
print('Доска позора, 3 спамеров: ', spam_count)
print(*result_list, sep = '\n')  #не влезает всё :(
