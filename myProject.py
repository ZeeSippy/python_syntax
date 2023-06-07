# Программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

# импортирование необходимых модулей
import hashlib as h
from tkinter import Tk, Label, Entry, Button, StringVar

# основная фнукция 
def pwdGenerator(pwd_str: str):
    # кодирование в байт строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = h.sha256(byte_str)
    # преобразование объекта хеш в обычную строку
    hex_str = hash_str.hexdigest()[:10]

    return hex_str

# тестирование функции
# while True:
#     pwd = input("Введите пароль: ")
#     if pwd == "stop":
#         break
#     print(pwdGenerator(pwd))

# объект окна
app = Tk()

# объекты для хранения строк
raw_pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
lbl = Label(text="Пароль: ")
lbl.grid(row=0, column=0)

# виджет поля ввода
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# виджет кнопки
def btn_func():
    res = pwdGenerator(raw_pwd.get())
    hash_pwd.set(res)
Button(text="ПУСК!", command=btn_func).grid(row=1, column=0)

# виджет поля вывода результата
Entry(textvariable=hash_pwd).grid(row=1, column=1)

# точка входа программы 
app.mainloop()