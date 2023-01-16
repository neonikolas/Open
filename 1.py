per_cent = {'ГПБ': 8.2, 'ОТК': 7.5, 'СБЕР': 8.0, 'ВТБ': 8.0}
money = int(input("Вводите сумму, которую желаете положить под проценты:"))

GPB = int((per_cent['ГПБ']) * (money/100))
OTK = int((per_cent['ОТК']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))
VTB = int((per_cent['ВТБ']) * (money/100))

deposit = [GPB, OTK, SBER, VTB]
print("Накопленные средства за год в каждом из банков =", deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
print(per_cent)