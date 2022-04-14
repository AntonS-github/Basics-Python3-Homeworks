'''
 *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
'''

numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}

def num_translate_adv (number: str):
    if number.istitle():
        number = number.lower()
        rus_number = numbers.get(number).capitalize()
    else: 
        rus_number = numbers.get(number)
    return  rus_number


if __name__ == "__main__":
    print(num_translate_adv('One'))
    print(num_translate_adv('six'))
