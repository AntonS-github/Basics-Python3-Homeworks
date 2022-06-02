'''4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.'''

class IntChecker(Exception):
    def __init__(self, input_el):
        self.input_el = input_el
        if input_el.isdigit():
            return True
        else:
            self.message = f'Вы ввели не числовое значение количества'
        super().__init__(self.message)  
        
class OfficeEquip:
    def __init__(self, model, price, wifi, color):
        self.model = model
        self.price = price
        self.wifi = wifi
        self.color = color
    
    def equip_storage(self):
        p_unit = {}
        s_unit = {}
        c_unit = {}
        storage = {'Принтеры': [],
                   'Сканеры': [],
                   'Копиры': []}
        e_type = input('Введите тип оборудования - принтер, сканер, копир: ')
        model = input('Введите модель оборудования: ')
        num = input('Введите кол-во оборудования: ')
        if num.isdigit():
            if e_type.lower() == 'принтер':
                p_unit[model] = num
                p_list
                storage['Принтеры'].append(p_unit)
            elif e_type.lower() == 'сканер':
                c_unit[model] = num
                storage['Сканеры'].append(c_unit)
            elif e_type.lower() == 'копир':
                s_unit[model] = num
                storage['Копиры'].append(s_unit)
            return storage   
        else:
            raise IntChecker(num)
class Printer(OfficeEquip):
    def __init__(self, model, price, wifi, color, num_sheets):
        super().__init__(model, price, wifi, color)
        self.num_sheets = num_sheets
    def __str__(self):
        return f'Printer: {self.model}, Price: {self.price}, WiFi: {self.wifi}, Color printing: {self.color}, printing speed: {self.num_sheets}'
        
class Scaner(OfficeEquip):
    def __init__(self, model, price, wifi, color, resolution):
        super().__init__(model, price, wifi, color)
        self.resolution = resolution
    def __str__(self):
        return f'Scaner: {self.model}, Price: {self.price}, WiFi: {self.wifi}, Color printing: {self.color}, resolution: {self.resolution}' 
        
class Copier(OfficeEquip):
    def __init__(self, model, price, wifi, color, auto_feed):
        super().__init__(model, price, wifi, color)
        self.auto_feed = auto_feed
    def __str__(self):
        return f'Copier: {self.model}, Price: {self.price}, WiFi: {self.wifi}, Color printing: {self.color}, auto feed: {self.auto_feed}'
        
canon_print = Printer('Canon', 250, False, False, 50)
hp_print = Printer('HP', 300, True, False, 70)
print(canon_print)
print(hp_print)
hp_scan = Scaner('HP Scan', 1000, True, True, 1920)
print(hp_scan)
xerox_copy = Copier('XEROX', 500, True, False, False)
print(xerox_copy)
print(canon_print.equip_storage())
