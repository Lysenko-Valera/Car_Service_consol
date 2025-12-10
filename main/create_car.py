from main.descriptor_car import CarDescriptor


class ChargingError(Exception):
    "Ошибка заряда батареи, если подзарядка батарее больше чем 100%"

class Car:
    '''Класс для инициализации авто и дальнейшей работы с ним.

.Класс который содержит атрибуты
brand: str,
model: str,
year: int,
mileage: int,
vin: str
,fuel_type: str,
engine_capacity: float,
gas_tank_capacity: int.
 Атрибуты отбираются по параментрам
которые описанны в на docstrings класса CarDescriptor файла descriptor_car.py

В классе есть подкласс ElectricCar в котором добавлены атрибуты   battery_kvtime: int, charge_lvl: int,
переопределены методы __str__ и __repr__, есть метод charge'''
    vin = CarDescriptor() # Создаем экземляры класса дескриптора для применения его
    year = CarDescriptor()
    fuel_type = CarDescriptor()
    engine_capacity = CarDescriptor()
    gas_tank_capacity = CarDescriptor()

    def __init__(self, brand: str, model: str, year: int, mileage: int, vin: str
                 ,fuel_type: int, engine_capacity: float, gas_tank_capacity: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.vin = vin
        self.fuel_type = fuel_type
        self.engine_capacity = engine_capacity
        self.gas_tank_capacity = gas_tank_capacity

    def __repr__(self):
        return f'''Класс Car.
        brand: str {self.brand}, model: str {self.model}, year: int {self.year}
        mileage: int {self.mileage}, vin: str {self.vin}'''

    def __str__(self):
        return f'''Приветсвую вас) Брэнд авто - {self.brand}
        Модель авто - {self.model}. Год авто {self.year}. Пробег - {self.mileage}.
        ВИН номер авто - {self.vin}'''

    def __eq__(self, other):
        if not isinstance(other, (int, Car)):
            raise TypeError('Ошибка сравнения. Справа должен быть тип int или Cloak')

        sc = other if isinstance(other, int) else other.mileage
        return self.mileage == sc

    def __hash__(self):
        return hash((self.brand, self.model))

    __age = 0 #Инкапсулируем атрибут где в дальнейшем через property добавляет get & set
    @property
    def set_or_get_age(self):
        self.__age = 2025 - self.year
        return self.__age

    @set_or_get_age.setter
    def set_or_get_age(self, new_age) -> int:
        self.__age = new_age

class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int, mileage: int, vin: str,
                    battery_kvtime: int, charge_lvl = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.vin = vin
        self.battery_kvtime = battery_kvtime
        self.charge_lvl = charge_lvl

    def __str__(self):
        return f'''Приветсвую вас) Брэнд авто - {self.brand}
        Модель авто - {self.model}. Год авто {self.year}. Пробег - {self.mileage}.
        ВИН номер авто - {self.vin}, емкость батареи - {self.battery_kvtime}. Заряд батареи - {self.charge_lvl}'''

    def __repr__(self):
        return f'''Класс Car.
        brand: str {self.brand}, model: str {self.model}, year: int {self.year}
        mileage: int {self.mileage}, vin: str {self.vin} 
        battery_kvtime: int {self.battery_kvtime}. charge_lvl: int {self.charge_lvl}'''

    def charge(self, charging: int) -> int:
        if charging > 100:
            raise ChargingError('Ошибка. Нельзя зарядить батарею больше чем на 100%')
        else:
            self.charge_lvl = charging
            return f'Вы зарядили машину на {charging}%'