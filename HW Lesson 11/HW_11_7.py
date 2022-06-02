'''7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность
полученного результата.'''

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x} + {self.y}i'
    def __add__(self, other):
        print('Сумма: ')
        x = self.x + other.x
        y = self.y + other.y
        return f'{x} + {y}i'
    def __mul__(self, other):
        print('Произведение: ')
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + other.x * self.y
        return f'{x} + {y}i'
z1 = Complex(2, 3)
z2 = Complex(3, 4)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
    
        