'''1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
#>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''

# >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# >>> m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}


import re

def email_parse(email):
    out_dict = {}
    EMAIL_PATTERN = re.compile(r'\w*@\w*\.')
    if EMAIL_PATTERN.match(email):
        out_dict['username'] = email.split('@')[0]
        out_dict['domain'] = email.split('@')[1]
    else:
        assert EMAIL_PATTERN.match(email), f'ValueError({email})'
    return print(out_dict)
email_parse('anvalsur@gmail.com')

