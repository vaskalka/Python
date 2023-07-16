''' Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N. '''

N = input("Введите число, до которого я посчитаю степени: ")

Degree = 1  # Степень двойки, с которой мы начнем 
CurrentValue = 0  # Переменная для фиксации текущего значения двойки в степени Degree  

print("Степени двойки до числа N: ")
while CurrentValue < int(N):
    CurrentValue = 2 ** Degree
    if CurrentValue < int(N):
        print(f"2^{Degree} = {CurrentValue}")
        Degree += 1
