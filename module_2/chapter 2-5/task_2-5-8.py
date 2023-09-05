# Дано 3-х значное число.  Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

num = int(input())
c = num % 10
b = (num % 10**2)//10
a = (num % 10**3)//10**2

print(a,b,c, sep='')
print(a,c,b, sep='')
print(b,a,c, sep='')
print(b,c,a, sep='')
print(c,a,b, sep='')
print(c,b,a, sep='')