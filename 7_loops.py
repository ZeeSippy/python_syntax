# *** Циклы ***

# Оператор цикла while

# Бесконечный цикл
# while True:
#     print("Hello")

# Цикл с условием
val_1 = 0

# while val_1 < 10:
#     print(f"value = {val_1}")
#     # инкремент
#     # длинный вариант
#     # val_1 = val_1 + 1
# # короткий вариант
# val_1 += 1

# while val_1 > -10:
#     print(f"value = {val_1}")
#     # декремент
#     # длинный вариант
#     # val_1 = val_1 - 1
#     # короткий вариант
#     val_1 -= 1

# прерывание цикла по дополнительному условию
a = 10
# while True:
#     print("Hello")

#     if a <= 0:
#         print("Bye bye!")
#         break

#     a -= 1

# while a > 0:
#     print("Hello")

#     if a == 5:
#         print("Bye-bye!")
#         break

#     a -= 1

# пропуск части кода тела цикла
val_2 = 0

# while val_2 < 20:
#     print(val_2)

#     val_2 += 1

#     if val_2 < 10:
#         continue

#     print("after")

val_2 = 0

# while val_2 < 20:
#     print(val_2)

#     val_2 += 1

#     if val_2 > 10:
#         continue

#     print("after")
\

# Оператор цикла for

# 1. Чтение значения итерируемого объекта по порядку
# 2. Каждое считанное значение присваивает в свою переменную
# 3. Выпаолняет код в своем теле\

list_0 = [26, 689, 1, 47, 0]

# for v in list_0:
#     v = v * 10
#     print(f"value = {v}")

# for v in [0, 10, 20, 30]:
#     print(v)

dict_0 = dict(a=100, b=200, c=300)

# print(dict_0)

# for i in dict_0.items():
#     print(i)

# for k, v in dict_0.items():
#     print(f"key = {k}, value = {v}")

# for k in dict_0.keys():
#     print(k)

# for v in dict_0.values():
#     print(v)

# Класс range()

r = range(-10, 10)
r = range(-5, 5, 2)
r = range(10)

# print(r)

# for v in r:
#     print(v)

for i in range(7):
    print(i)

# *** ПРОЧИТАТЬ ! ! ! ***
# генератор списка
# генератор словаря