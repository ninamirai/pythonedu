# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.

num0 = int(input())
num1 = int(input())

sum = num0 + num1
difference = num0 - num1
multiplication = num0 * num1

print(num0, '+', num1, '=', sum)
print(num0, '-', num1, '=', difference)
print(num0, '*', num1, '=', multiplication)