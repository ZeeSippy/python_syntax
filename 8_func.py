# *** Функции ***

# создание функции
def func_1():
    print("hello, from function!")

def func_2(arg_0, arg_1):
    res = arg_0 + arg_1
    print(res)

def func_3(arg_0, arg_1):
    res = arg_0 + arg_1
    return res

# вызов функции
# func_1()
# func_2(2, 10)
# r = func_3(2, 10)
# print(r)


# *** Классы ***

# создание класса
class Human:
    # метод-конструктор
    def __init__(self, name, age_arg) -> None:
        # атрибуты (свойства)
        self.name = name
        self.age = age_arg

    # метод - функция экземпляра (объекта)
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# создание экземпляра (объекта) класса Human
p0 = Human("Sergey", 24)
p1 = Human("Mark", 22)

# p1.name = "Mark"
# p1.age = 22

# print(p0.name, p0.age)
# print(p1.name, p1.age)

p0.info()
p1.info()

# Изучить аргументы функций (значения по умолчанию, позиционная и именованная передача параметров)
# принципы ООП (наследование, полиморфизм, инкапсуляция, композиция)
