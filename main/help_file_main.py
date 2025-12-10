import pandas as pd
import tkinter as tk
from tkinter import Entry
from tkinter import messagebox, Button
from PIL import Image, ImageTk
from main import create_car
from main.helpers_photo import resource_path


def button_service_prices():
    df = pd.read_excel(r'C:\Users\Анастасия\OneDrive\Документы\Услуги_цены.xlsx')

    service_window = tk.Toplevel()
    service_window.title('Список услуг и цен')
    service_window.geometry('460x450')
    service_window.resizable(width=False, height=False)
    service_window.config(bg='black')
    label = tk.Label(service_window, text='Cписок улуг и цен',
                     font=('Arial', 15, 'bold'), bg='orange', fg='black')
    label.pack()

    label = tk.Label(service_window, text=df,
                     font=('Arial', 10, 'bold'), bg='black', fg='white')
    label.pack()


def button_create_order():
    def button_cr_cr():
        brand = str(brand_auto.get())
        model = str(model_auto.get())
        year = int(year_auto.get())
        mileage = int(mileage_auto.get())
        vin = str(vin_auto.get())
        fuel_type = int(fuel_type_auto.get())
        engine_capacity = float(engine_capacity_auto.get())
        gas_tank_capacity = int(gas_tank_capacity_auto.get())
        types_services = str(types_services_auto.get())
        price_services_intermediate = str(price_one_services.get())
        mechanik = int(mechanik_auto.get())
        price_services = sum([int(i) for i in price_services_intermediate.split(',')])
        create_car.Car(brand, model, year, mileage, vin, fuel_type, engine_capacity,
                       gas_tank_capacity)

        dict_order = {'brand': [brand], 'model': [model], 'year': [year], 'mileage': [mileage],
                      'vin': [vin], 'fuel_type': [fuel_type], 'engine_capacity': [engine_capacity],
                      'gas_tank_capacity': [gas_tank_capacity], 'types_services': [types_services],
                      'price_services': [price_services], 'mechanik': [mechanik]}

        file_path = r'C:\Users\Анастасия\OneDrive\Desktop\Заказы.xlsx'
        new_df = pd.DataFrame(dict_order)
        try:
            old = pd.read_excel(file_path)
            df = pd.concat([old, new_df], ignore_index=True)
        except FileNotFoundError:
            df = new_df
        df.to_excel(file_path, index=False)



    def order_help(txt: str):
        label = tk.Label(order_window, text=txt,
                         font=('Arial', 10, 'bold'), bg='black', fg='white')
        label.pack()
        entry = Entry(order_window, font=('Arial', 10), width=25, justify='left')
        entry.pack()
        return entry

    order_window = tk.Tk()
    order_window.title('Создание заказа')
    order_window.geometry('700x700')
    order_window.resizable(width=False, height=False)
    order_window.config(bg='black')

    label = tk.Label(order_window, text='Создание заказа',
                     font=('Arial', 25, 'bold'), bg='orange', fg='black')
    label.pack()

    brand_auto = order_help('Введите брэнд авто:')
    model_auto = order_help('Введите модель авто:')
    year_auto = order_help('Введите год авто:')
    mileage_auto = order_help('Введите пробег авто:')
    vin_auto = order_help('Введите вин номер авто типа [1_][**********][6_] где _-цифра, а *-цифра|буква":')
    fuel_type_auto = order_help('Введите тип топлива 1 - бензин, 2 - дизель, 3 - газ:')
    engine_capacity_auto = order_help('Введите объем двигателя авто вещественным числом:')
    gas_tank_capacity_auto = order_help('Введите объем бензобака авто:')
    types_services_auto = order_help('Виды услуг')
    price_one_services = order_help('Цена за одну услугу через запятую цену')
    mechanik_auto = order_help('id механника авто')

    button_order_cr = Button(order_window, command=button_cr_cr, text='Сохранить данные',
                             font=('Arial', 20), bg='lime')
    button_order_cr.pack()



def button_list_mechanik():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    df = pd.read_excel(r'C:\Users\Анастасия\OneDrive\Документы\Механники.xlsx')

    mechanick_window = tk.Tk()
    mechanick_window.title('Список механников')
    mechanick_window.geometry('700x250')
    mechanick_window.resizable(width=False, height=False)
    mechanick_window.config(bg='black')

    label = tk.Label(mechanick_window, text='Cписок механников и их занятость',
                     font=('Arial', 15, 'bold'), bg='orange', fg='black')
    label.pack()

    label = tk.Label(mechanick_window, text=df,
                     font=('Arial', 10, 'bold'), bg='black', fg='white')
    label.place(x=0, y=35)


def button_see_order():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    df = pd.read_excel(r'C:\Users\Анастасия\OneDrive\Завершенные_заказы.xlsx')

    order_see_window = tk.Toplevel()
    order_see_window.title('Завершенные заказы')
    order_see_window.geometry('460x450')
    order_see_window.config(bg='black')

    label = tk.Label(order_see_window, text='Завершенные заказы',
                     font=('Arial', 20, 'bold'), bg='orange', fg='black')
    label.pack()

    label = tk.Label(order_see_window, text=df,
                     font=('Arial', 10, 'bold'), bg='black', fg='white')
    label.pack()


def comm_butt_ord_cplt(index_entry):
    index_user = int(index_entry.get())

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    df_orders = pd.read_excel(r'C:\Users\Анастасия\OneDrive\Desktop\Заказы.xlsx')
    df_orders.columns = [c.lower() for c in df_orders.columns]

    if index_user not in df_orders.index:
        messagebox.showerror("Ошибка", "Такого ID нет!")
        return

    vin = str(df_orders.loc[index_user, "vin"])
    service = str(df_orders.loc[index_user, "types_services"])
    df_orders = df_orders.drop(index_user)
    df_orders.to_excel(r'C:\Users\Анастасия\OneDrive\Desktop\Заказы.xlsx', index=False)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    file_path = r'C:\Users\Анастасия\OneDrive\Завершенные_заказы.xlsx'
    try:
        df_completed = pd.read_excel(file_path)
        df_completed.columns = [c.lower() for c in df_completed.columns]
    except FileNotFoundError:
        df_completed = pd.DataFrame(columns=["vin", "services"])

    if vin in df_completed["vin"].astype(str).values:
        mask = df_completed["vin"].astype(str) == vin
        old_text = df_completed.loc[mask, "services"].iloc[0]
        df_completed.loc[mask, "services"] = old_text + ", " + service
    else:
        df_completed.loc[len(df_completed)] = [vin, service]

    df_completed.to_excel(file_path, index=False)
    messagebox.showinfo("Успех", "Заказ завершён!")



def order_complete():
    order_complete_window = tk.Toplevel()
    order_complete_window.title('Завершение заказа')
    order_complete_window.geometry('460x450')
    order_complete_window.config(bg='black')
    order_complete_window.resizable(width=False, height=False)
    label = tk.Label(order_complete_window, text='Завершить заказ по id заказа',
                     font=('Arial', 22, 'bold'), bg='orange', fg='black')
    label.pack()
    label = tk.Label(order_complete_window, text='Введите id заказа',
                     font=('Arial', 15, 'bold'), bg='black', fg='white')
    label.pack()
    index = Entry(order_complete_window, font=('Arial', 20, 'bold'))
    index.pack()
    button_order_complete = Button(order_complete_window, command=lambda: comm_butt_ord_cplt(index), text='Завершить',
                                   font=('Arial', 20, 'bold'), bg='lime', fg='black')
    button_order_complete.pack()


def active_order():
    active_order_window = tk.Tk()
    active_order_window.config(bg='black')
    active_order_window.title('Активные заказы')
    active_order_window.geometry('500x500')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    df = pd.read_excel(r'C:\Users\Анастасия\OneDrive\Desktop\Заказы.xlsx')
    label = tk.Label(active_order_window, text='Активные заказы', font=('Arial', 25, 'bold'),
                     bg='orange', fg='black')
    label.pack()
    text = tk.Text(active_order_window,
                   font=("Consolas", 11),
                   bg="black",
                   fg="white",
                   wrap="none",
                   width=120,
                   height=25)

    scroll_y = tk.Scrollbar(active_order_window, orient="vertical", command=text.yview)
    scroll_x = tk.Scrollbar(active_order_window, orient="horizontal", command=text.xview)

    text.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    text.pack(fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")

    text.insert("1.0", df.to_string(index=False))
    text.configure(state="disabled")

def main():
    main_window = tk.Tk()
    main_window.title('Автосервис')
    main_window.geometry('1000x700')
    main_window.resizable(width=False, height=False)

    img_path = resource_path('main/mersedes_photo_label.jpg')
    img = Image.open(img_path)
    img = img.resize((1000, 700))
    bg = ImageTk.PhotoImage(img)

    label = tk.Label(main_window, image=bg)
    label.image = bg
    label.place(x=0, y=0, relwidth=1, relheight=1)

    label = tk.Label(main_window, text='Система управления админ панелью',
                 font=('Arial', 35, 'bold'), bg='orange')
    label.pack()

    label = tk.Label(main_window, text='Выберите что хотите сделать нажав кнопку:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white')
    label.pack()

    button_list_services = Button(main_window, command=button_service_prices, text='Услуги и цены',
                              font=('Arial', 18, 'bold'), bg='green', fg='black')
    button_list_services.place(x=0, y=100)

    button_order_cr = Button(main_window, command=button_create_order, text='Создать заказ',
                              font=('Arial', 18, 'bold'), bg='green', fg='black')
    button_order_cr.place(x=804, y=100)
    button_mechanik = Button(main_window, command=button_list_mechanik, text='Показ механников',
                              font=('Arial', 18, 'bold'), bg='green', fg='black')
    button_mechanik.place(x=0, y=150)

    button_stop_order = Button(main_window, command=order_complete, text='Завершить заказ',
                              font=('Arial', 18, 'bold'), bg='green', fg='black')
    button_stop_order.place(x=767, y=150)

    button_see_service = Button(main_window, command=button_see_order, text='Завершенные заказы',
                              font=('Arial', 22, 'bold'), bg='green', fg='black')
    button_see_service.pack()

    button_active_order = Button(main_window, command=active_order, text='Активные заказы',
                                 font=('Arial', 26, 'bold'), bg='red', fg='black')
    button_active_order.pack()

