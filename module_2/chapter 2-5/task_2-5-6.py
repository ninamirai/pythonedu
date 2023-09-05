# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

minutes = int(input())

hours = minutes//60
minutes_ost = minutes%60
print(minutes, "мин - это", hours, "час", minutes_ost, "минут.")