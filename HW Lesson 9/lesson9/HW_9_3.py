'''3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''
class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage,
                        'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        full_name = f'Работника зовут: {self.surname} {self.name}'
        return full_name
    def get_total_income(self):
        total_income = sum(self._income.values())
        return f'Общий доход работника: {total_income}'

person_1 = Position('Иван', 'Петров', 10000, 3000)
print(person_1.get_full_name())
print(person_1.get_total_income())