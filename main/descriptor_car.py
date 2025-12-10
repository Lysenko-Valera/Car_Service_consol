from tkinter import messagebox


class VINCarError(Exception):
    """Исключение для вин номера авто по параметрам:
     _ - цифра * буква или цифра. vin должен быть типа "[_][**********][______]"
    Среди цифр или букв (*) должно быть 2 подряд идущих цифры."""

class ErrorCarCystem(Exception):
    """Исключение если объем двигателя меньше 0.1 л или более 20 литров,
    а объем топливного бака не более 450 л и не менее 3 л"""

class CarDescriptor:
    '''Создаем класс CarDescriptor, который будет использоваться в модуле create_car
    для атрибутов vin: str
     и year: int.
    Параметры для валидации vin, year
    _ - цифра * буква или цифра. vin должен быть типа "[_][**********][______]"
    Среди цифр или букв (*) должно быть 2 подряд идущих цифры.
    year - должен быть целым числом и не более 2025 и не менее 1920.
    fuel_type: int который должен быть от 1 до 3 вкл
    engine_capacity: float должен быть от 0.1 до 20.0
    gas_tank_capacity: int должен быть более 3-х но не менее 450
    '''
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validation_values(self.name, value)
        instance.__dict__[self.name] = value

    @classmethod
    def validation_values(cls, name: str, value: int | str):
        if name == '__year':
            if not isinstance(value, int):
                messagebox.showerror('Ошибка.', 'Год авто должен быть целым числом')
            if 1920 >= value >= 2025:
                messagebox.showerror('Ошибка.', 'Год авто должен быть в пределе'
                                   ' 1920 по 2025 год включительно')

        if name == '__vin':
            if not isinstance(value, str):
                messagebox.showerror('Ошибка.', 'ВИН номер авто должен быть строкой')
            if len(value) != 17:
                messagebox.showerror('Ошибка.', 'Вин номер авто должен состоять минимум из 17 символов')
            num_check = (value[1:3].isdigit() or value[3:5].isdigit()
                        or value[5:7].isdigit() or value[7:9].isdigit()
                        or value[9:11].isdigit())
            if (value.isalnum() and value[0].isdigit() and value[11:].isdigit()
                and not num_check):
                messagebox.showerror('Ошибка.',
                                     'Не верный формат записи VIN: [_][**********][______]')

        if name == '__fuel_type':
            if not isinstance(value, int):
                messagebox.showerror('Ошибка.', 'Тип топлива должен быть числом 1 - бензин, 2 - '
                                'дизель, 3 - газ')

            if 3 < value < 1:
                messagebox.showerror('Ошибка.', 'Тип топлива должен быть числом 1 - бензин, 2 - '
                                'дизель, 3 - газ')

        if name == '__engine_capacity':
            if not isinstance(value, float):
                messagebox.showerror('Ошибка.', 'Объем двигателя должен быть дробным числом.')
            if 20.0 < value < 0.1:
                messagebox.showerror('Ошибка.',
                                     'Объем двигателя должен быть не менее 0.1 и не более 20 л')

        if name == '__gas_tank_capacity':
            if not isinstance(value, int):
                messagebox.showerror('Ошибка.' ,'Объем топливного бака должен быть целым числом')
            if not(3 < value < 450):
                messagebox.showerror('Ошибка.',
                                     'объем топливного бака должен быть более 3 л и не более 450 л')

