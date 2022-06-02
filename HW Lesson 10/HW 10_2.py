'''2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.'''

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h
    @property
    def coat(self):
        return self.v / 6.5 + 0.5
    @property
    def suit(self):
        return 2*self.h + 0.3
    @property
    def consumption(self):
        return self.h*self.v   

sewing = Clothes(5, 6)
print(sewing.coat) 
print(sewing.suit)
print(sewing.consumption) 
     
        