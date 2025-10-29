from dataclasses import dataclass


class InvalidServiceError(Exception):
    """Отлавливает все ошибки связанные с сервисом такие как:
    Не верный формат имени механника, неверная цена, неверное продолжительность часов,
    неверный тип сервисной услуги"""

@dataclass
class Service:
    """Dataclass имеющий атрибуты name - имя, price - цена, duration_hours - продолжительность работы
    service_type - тип сервисной услуги, имеет магический метод __add__
    Класс имеет __post_init__ где проверяется тип данных который ввел пользователей"""
    name: str
    price: list
    duration_hours: float
    service_type: list

    def __post_init__(self):
        '''Магический метод должен который вызывается перед инициализацией,
        он проверяет name, price, duration_hours, service_type на то что бы они соответсвовали
        нужному типу данных.'''
        if not isinstance(self.name, str):
            raise InvalidServiceError('Ошибка. Имя должно быть строкой')
        if not isinstance(self.price, list) or self.price < 0:
            raise InvalidServiceError('Ошибка. Цена должна быть списком')
        if not isinstance(self.duration_hours, float) or self.duration_hours < 0:
            raise InvalidServiceError('Ошибка. Кол-во времени должно быть вещественным числом')
        if not isinstance(self.service_type, list):
            raise InvalidServiceError('Ошибка. Тип сервисной услуги должен быть списком')

    def __add__(self, other):
        return self.price + other


# s = Service('Harry', 1003.7, 9.0, 'Замена масла')