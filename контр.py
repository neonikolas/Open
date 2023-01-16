per_cent = {'ТБК': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Вводите сумму, которую желаете положить под проценты:"))

TBK = int((per_cent['ТБК']) * (money/100))
SKB = int((per_cent['СКБ']) * (money/100))
VTB = int((per_cent['ВТБ']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))

deposit = [TBK, SKB, VTB, SBER]
print("Накопленные средства за год в каждом из банков =", deposit)

print("Максимальная сумма, которую вы можете заработать:", max(deposit))
print(per_cent)