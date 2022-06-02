'''4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.'''

from random import randint
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Машина: {self.name}\n'
              f'Цвет: {self.color}\n'
              f'Макс. скорость: {self.speed}\n'
              f'Принадлежит полиции: {is_police}')
    def go(self):
        print("Let's GO!")
    def stop(self):
        print('АСТАНАВИЛИСЬ!')
    def turn(self, direction):
        print(f'Поворачиваем {direction}')
    def show_speed(self):
        self.current_speed = randint(50, 200)
        return print(f'Текущая скорость: {self.current_speed}')
class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
    def show_speed(self):
        self.current_speed = randint(50, 65)
        if self.current_speed >= 60:
            print(f'Too high speed for TownCar {self.current_speed} км/ч')
        else: print(f'Текущая скорость: {self.current_speed}')
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
    def show_speed(self):
        self.current_speed = randint(30, 50)
        if self.current_speed >= 40:
            print(f'Too high speed for TownCar {self.current_speed} км/ч')
        else: print(f'Текущая скорость: {self.current_speed}')
class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)

my_car = Car(380, 'чёрный', 'Дэу Нексия')
my_car.go()
my_car.turn('налево')
my_car.show_speed()
my_car.stop()
print('------Городская: ---------')
town_car = TownCar(180, 'жёлтый', 'hyundau solaris')
town_car.show_speed()
print('------Рабочая: ---------')
work_car = WorkCar(40, 'красный', 'Камаз')
work_car.show_speed()
print('------Спортивная: ---------')
sport_car = SportCar(370, 'золотой', 'Lambo')
sport_car.show_speed()
print('------Полицай: ---------')
police_car = PoliceCar(100, 'серый', 'Ford')
police_car.show_speed()

