'''2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class ZeroDivision(Exception):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            self.message = f'Деление на ноль!!!'
        else:
            return self.numerator / self.denominator
        super().__init__(self.message, self.numerator, self.denominator)
a = 6
b = 0
if b == 0:
    raise ZeroDivision(a, b)
else:
    print(a / b)

            