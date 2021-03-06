'''5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.'''
import cv2
class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Рисуем")
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Рисуем ручкой")
class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Рисуем карандашом")
class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Рисуем маркером")
a = Stationary('Картина')
a.draw()
b = Pen('Картина')
b.draw()
c = Pencil('Картина')
c.draw()
d = Handle('Картина')
d.draw()