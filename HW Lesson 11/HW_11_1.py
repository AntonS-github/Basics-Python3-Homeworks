'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.'''
class Date:
    
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = dd_mm_yy
    @classmethod
    def extraction(cls, dd_mm_yy):
        res = str(dd_mm_yy).split('-')
        ext_list = []
        for i in res:
            if i != '-':
                ext_list.append(i)
        return int(''.join(ext_list))
    @staticmethod
    def validation(dd_mm_yy):
        res = str(dd_mm_yy).split('-')
        if 0 < int(res[0]) <= 31:
            if 0 < int(res[1]) <= 12:
                if 0 < int(res[2]) <= 2022:
                    return f'The date is vaild {dd_mm_yy}'
                else:
                    raise ValueError('Alarm! Invalid year value')
            else:
                raise ValueError('Alarm! Invalid month value')
        else:
            raise ValueError('Alarm! Invalid day value')
                    

print(Date.extraction('22-11-2012'))
print(Date.validation('31-13-2022'))