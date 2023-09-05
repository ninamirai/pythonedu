# Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.

price_of_monitor = int(input())
price_of_system = int(input())
price_of_keyboard = int(input())
price_of_mouse = int(input())

pc = price_of_monitor + price_of_system + price_of_keyboard + price_of_mouse
print(3*pc)