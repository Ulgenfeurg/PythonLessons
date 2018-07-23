# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.

# Задача-1:
Fruits = ["яблоко", "банан", "киви", "арбуз"]

print("{}.{:>6}".format(1, Fruits[0]))
print("{}.{:>6}".format(2, Fruits[1]))
print("{}.{:>6}".format(3, Fruits[2]))
print("{}.{:>6}".format(4, Fruits[3]))


# Задача-2:
Ramm = {"Till", "Richard", "Oliver", "Flake", "Cristoph", "Paul"}
Guitarists = {"Paul", "Richard", "Oliver", "James", "Kirk"}
print(Ramm&Guitarists)

# Задача-3:

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100500]
New_Numbers = []
for number in Numbers:
    if number % 2 == 0:
        New_Numbers.append(number / 4)
    else:
        New_Numbers.append(number * 2)

print(New_Numbers)
