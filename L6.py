# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# first_num = int(input("Укажите первое число: "))
# increment = int(input("Укажите разность элементов: "))
# count_of_numbers = int(input("Укажите количество элементов: "))
# result = first_num
# i = 0
# while i <= count_of_numbers:
#     print(result, end = ' ')
#     result += increment
#     i += 1



# Задача 32: Определить элементs массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 1
# 19
# Вывод: [1, 9, 13, 14, 19]

list1 = [int(i) for i in input('Введите массив чисел через пробел: ').split(' ')]
start_number = int(input('Введите начальное число: '))
end_number = int(input('Введите последнее число: '))
list2 = [i for i in list1 if start_number <= i <= end_number]
print(list2)