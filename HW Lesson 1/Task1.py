"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""



#РЕШЕНИЕ БЕЗ ЦИКЛОВ
def naive_realisation():
     duration = int(input('Введите продолжительность в секундах: '))
     days = duration // 86400
     hours = duration // 3600 - days * 24
     minutes = duration // 60 - days * 1440 - hours * 60
     seconds = duration - days * 86400 - hours * 3600 - minutes * 60
     if days >= 1:
         print(days, 'дней', hours, 'часов', minutes, 'минут', seconds, 'секунд')
     elif hours >= 1 and days < 1:
         print(hours, 'часов', minutes, 'минут', seconds, 'секунд')
     elif minutes >= 1 and hours < 1:
         print(minutes, 'минут', seconds, 'секунд')
     else:
         print(seconds, 'секунд')
     return
naive_realisation()


def one_cycle_realisation():
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    dur = 0
    while True:
        dur = int(input('Введите продолжительность в секундах: '))
        days = dur // 86400
        hours = dur // 3600 - days * 24
        minutes = dur // 60 - days * 1440 - hours * 60
        seconds = dur - days * 86400 - hours * 3600 - minutes * 60
        if days >= 1:
            total_time = print(days, 'дней', hours, 'часов', minutes, 'минут', seconds, 'секунд')
        elif hours >= 1 and days < 1:
            total_time = print(hours, 'часов', minutes, 'минут', seconds, 'секунд')
        elif minutes >= 1 and hours < 1:
            total_time = print(minutes, 'минут', seconds, 'секунд')
        else:
            total_time = print(seconds, 'секунд')
    return
one_cycle_realisation()