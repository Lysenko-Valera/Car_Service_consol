from main.mechanik import Mechanic


class OrderNotFoundError(Exception):
    """Отлавливает все ошибки связанные с заказом:
    Не верный формат id, car, mechanic, services, status, total_cost"""

class Order(Mechanic):
    """Класс созданный для заказа услуги. Содержит атрибуты:

    order_id: int - id заказа, car: list - машина (с ее характеристиками)
    mechanic: list - механик (с его характеристиками), services: str - тип услуги
    status: str - статус заказа (на каком этапе) total_cost: int - общая стоимость

    Содержит магические методы __str__, __repr__, __eq__. А так же метод
        calculate_total который высчитывает конечную сумму"""
    def __init__(self, order_id: int, car: list, mechanic: list, services: str
                 , status: str, total_cost: float):
        if not isinstance(car, list):
            raise OrderNotFoundError('Ошибка. Машина должна быть списком')
        if not isinstance(mechanic, list):
            raise OrderNotFoundError('Ошибка. Механик должен быть списком')
        if not isinstance(services, str):
            raise OrderNotFoundError('Ошибка. Тип сервисной услуги должен быть строкой')
        if not isinstance(status, str):
            raise OrderNotFoundError('Ошибка. Статус заказа должен быть строкой')
        if not isinstance(total_cost, float):
            raise OrderNotFoundError('Ошибка. Конечная цена должна быть вещественным числом')

        self.order_id = self.generation_id()
        self.car = car
        self.mechanic = mechanic
        self.services = services
        self.status = status
        self.total_cost = self.calculate_total()

    def calculate_total(self):
        self.total_cost = sum(self.price) + 0.0

    def __str__(self):
        return f"""Приветсвую вас. id заказа - {self.order_id},
    машина - {self.car}
    механик - {self.mechanic}
    сервисная услуга - {self.services}
    статус ремонта - {self.status}
        конечная цена за ремонт: {self.total_cost}"""

    def __repr__(self):
        return f"""Класс Order 
    order id: int {self.order_id}
    car: list {self.car}
    mechanic: list {self.mechanic}
    services: str {self.services}
    status: str {self.status}
    total_cost: float {self.total_cost}"""

    def __eq__(self, other):
        return self.total_cost == other

