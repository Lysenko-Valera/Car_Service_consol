import tkinter as tk
from tkinter import Entry, Button
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice
from main import help_file_main
from main.helpers_photo import resource_path

password_list_administrators = {'goroh008': 639217, 'magnit01': 963521,
                                'kniga771': 445612} #Логины и пароли администраторов
dict_capcha = {'68ㄥ9ᄅ': 98762, '6ㄥƐᄅ8': 97328, '9ㄥㄥƐᄅ': 97732, 'ᄅᄅ98Ɩ': 22981, 'ㄣ8ㄣᄅㄥ': 48427} #Капча
list_capcha = ['68ㄥ9ᄅ', '6ㄥƐᄅ8', '9ㄥㄥƐᄅ', 'ᄅᄅ98Ɩ', 'ㄣ8ㄣᄅㄥ']
correct_num_capcha = [98762, 97328, 67732, 22681, 48427]
count = 0
check = False


def checking_before_captcha(login, password):
    'Смотрит что бы пароль был введен верно и выводит количесво оставшихся попыток, если попыток 0 вызывает капчу'
    global count, check
    list_password = list(password_list_administrators.values())

    if password in list_password:
        index = list_password.index(password)
        name = list(password_list_administrators.keys())[index]
        check = True
        messagebox.showinfo('Добро пожаловать', f'Вы вошли в систему как {name}')
        count = 0
        window.destroy()
        help_file_main.main()
        return

    count += 1
    messagebox.showerror('Ошибка.',f'Неверный пароль. Осталось {3-count} попыток')

    if count >= 3:
        capcha(login, password)


def capcha(login, password):
    global count
    capcha_text = choice(list_capcha)
    correct_num = dict_capcha[capcha_text]

    capcha_window = tk.Tk()
    capcha_window.title('Капча')
    capcha_window.geometry('650x200')

    label_capcha = tk.Label(capcha_window, text='Вы ввели пароль неверное более 3-х раз и попали на проверку',
                     font=('Arial', 15, 'bold'), bg='red')
    label_capcha.pack()
    label_capcha = tk.Label(capcha_window, text=f'Введите цифры показанные на экране ниже \n{capcha_text}',
                     font=('Arial', 12, 'bold'), bg='red')
    label_capcha.pack()

    entry_capcha = Entry(capcha_window, font=('Arial', 20), width=20, justify='left')
    entry_capcha.pack()


    def check_capcha():
        'Функция для проверки капчи, выводит ошибки если что то неверно'

        try:
            capcha_num = int(entry_capcha.get())
        except ValueError:
            messagebox.showerror('Ошибка.', f'Вводите только цифры перевернув их')
            return

        if capcha_num == correct_num:
            messagebox.showinfo('Вы прошли капчу', 'Введите пароль заново')
            count = 0
            capcha_window.destroy()
            count = 0
        else:
            messagebox.showerror('Ошибка', 'Вы не верно ввели цифры, попробуйте заново')
            capcha_window.destroy()
            capcha(login, password)

    button_capcha = Button(capcha_window, command=check_capcha, text='Отправить',
                           font=('Arial', 18), bg='lime')
    button_capcha.pack()



def send_data():
    'Функция считывает данные которые пользователь ввел в поле entry, вызывает ошибку в случае не верного формата'

    login = login_input.get()
    try:
        password = int(password_input.get())
    except ValueError:
        messagebox.showerror('Ошибка','Пароль должен быть числом')
        return
    checking_before_captcha(login, password)



window = tk.Tk()
window.title('Автосервис')
window.geometry('1000x700')
window.resizable(width=False, height=False)
window.config(bg = '')

img_path = resource_path('main/mersedes_photo_label.jpg')
img = Image.open(img_path)
img = img.resize((1000, 700))
bg = ImageTk.PhotoImage(img)

label = tk.Label(window, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(window, text='Доброго пожаловать в систему.',
                 font=('Arial', 35, 'bold'), bg='orange')
label.pack()
label = tk.Label(window, text='Введите логин:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white', anchor='w')
label.pack(fill='x')

login_input = Entry(window, font=('Arial', 20), width=25, justify='left')
login_input.pack()

label = tk.Label(window, text='Введите пароль:',
                 font=('Arial', 20, 'bold'), bg='black', fg='white', anchor='w')
label.pack(fill='x')

password_input = Entry(window, font=('Arial', 20), width=25, justify='left')
password_input.pack()

button_login_pwrd = Button(window, command=send_data, text='Войти', font=('Arial', 30), bg='lime')
button_login_pwrd.pack()

if '__name__' == '__main__':
    window.mainloop()