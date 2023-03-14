'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом
. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть
'''

from random import randint

n = int(input("Введите количество монеток: "))
gerb_side = 0
reshka_side = 0

for i in range(n):
    monet = randint(0, 1)
    if monet == 0:
        reshka_side += 1
    else:
        gerb_side += 1

if reshka_side > gerb_side:
    vivod = reshka_side - gerb_side
else:
    vivod = gerb_side - reshka_side


print(f"{gerb_side} монеток упало гербом вверх, {reshka_side} монеток упало решкой вверх, {vivod} требуется перевернуть монет")