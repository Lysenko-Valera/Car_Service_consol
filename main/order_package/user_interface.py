from main.order_package.mechanik import Mechanic
from main.order_package.service import Service, InvalidServiceError
from main.order_package.create_car import Car, CarDescriptor, ChargingError, ElectricCar
from main.order_package.descriptor_car import CarDescriptor
from main.order_package.workshop_create import Workshop
from time import time
from random import choice


class CapchaError(Exception):
    '''Ошибка возникает когда пользователь неверно прошел капчу'''


password_list_administrators = {'Горшков Горох Горохович': 639217, 'Магний Магнит Магнитович': 963521,
                                'Книжков Книга Книгович': 445612, 'Шурупкин Шуруп Шурупович': 689438,
                                'Глава Главарь Главаривич': 337512}
list_password = [639217, 963521, 445612, 689438, 337512]
dict_capcha = {'68ㄥ9ᄅ': 98762, '6ㄥƐᄅ8': 97328, '9ㄥㄥƐᄅ': 97732, 'ᄅᄅ98Ɩ': 22981, 'ㄣ8ㄣᄅㄥ': 48427}
list_capcha = ['68ㄥ9ᄅ', '6ㄥƐᄅ8', '9ㄥㄥƐᄅ', 'ᄅᄅ98Ɩ', 'ㄣ8ㄣᄅㄥ']
correct_num_capcha = [98762, 97328, 67732, 22981, 48427]
count = 0
count_capcha = 0
password = None
name = None
check = False


def car_registration():
    print('''Вы выбрали номер действия 1 т.е регистрация авто. Заполните следующие данные ниже, при ошибке все прийдется начать сначала''')
    brand_car = str(input('Введите брэнд авто: '))
    model_car = str(input('Введите модель авто: '))
    age_car = int(input('Введите год авто: '))
    mileage_car = int(input('Введите пробег авто: '))
    vin_car = str(input('Введите вин номер авто типа [_][**********][______] где _-цифра, а *-цифра|буква": '))
    fuel_type_car = int(input('Введите тип топлива 1 - бензин, 2 - дизель, 3 - газ: '))
    engine_capacity_car = float(input('Введите объем двигателя авто вещественным числом: '))
    gas_tank_capacity_car = int(input('Введите объем бензобака авто: '))


def add_mechanic():
    print('''Вы выбрали номер действия 2 т.е добавление механика. Заполните следующие данные ниже, при ошибке все прийдется начать сначала''')
    name_mechanic = str(input('Введите имя механика: '))
    specialization_mechanic = str(input('Введите специализацию механика: '))
    experience_years_mechanic = float(input('Введите опыт работы мехвника, опыт работы должен быть вещественным числом:'))


def check_num_command(num):
    if num == 1:
        car_registration()
    if num == 2:
        add_mechanic()
    if num == 3:
        pass
        

def capcha():
    global count_capcha, count
    count_capcha += 1
    print('Вы неверно ввели пароль 3 и более раз пройдите проверку')
    time_begin_capcha = time()
    capcha_text = choice(list_capcha)
    capcha_num = int(input(f'''Введите цифры показанные ниже
    {capcha_text}
    Ввод производить в это поле: '''))
    time_end_capcha = time()
    difference_time = time_end_capcha - time_begin_capcha
    correct_num = dict_capcha[capcha_text]
    if 3 > difference_time or difference_time > 100 or capcha_num != correct_num:
        if count_capcha == 3:
            raise CapchaError('Ошибка. Вы не прошли проверку более 3-х раз запустите программу заново')
        else:
            capcha()
    else:
        print('Вы прошли капчу, можете занаво ввести пароль')
        count = 0
        checking_before_captcha()


def checking_before_captcha():
    global list_password, count, password, name, check
    if count < 3:
        count += 1
        print(f'Ведите пароль у вас осталось еще {4 - count} попыток')
        password = int(input('Введите ваш пароль от системы: '))
        if password in list_password:
            value_password = list(password_list_administrators.values())
            key_password = list(password_list_administrators.keys())
            index = value_password.index(password)
            name = key_password[index]
            check = True
        if password not in list_password:
            checking_before_captcha()
    else:
        capcha()


print('''Добро пожаловать в Электронную сервисную систему ^^Fergus System^^
Тут вы можете зарегестрировать машину, добавить механика, создать заказ и завершить его''')
checking_before_captcha()

if check == True:
    print(f'''{name} Добро пожаловать в систему ^^Fergus System^^''')
    print('''Возможности приложения:
Введите <1> если хотите зарегистрировать новую машину)
Введите <2> если хотите добавить механика)
Введите <3> если хотите создать заказ)
Введите <4> если хотите завершить заказ)
Введите <5> если хотите показать статистику)''')
num_command = int(input('Введите номер для создания действия'))





