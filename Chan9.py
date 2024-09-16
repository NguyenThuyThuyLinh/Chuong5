# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:25:03 2024

@author: Nguyen Thuy Thuy Linh
"""
Chia9 = []

for number in range(2020, 3839):
    if number % 2 == 0:
        Chia9.append(number)

divisible_by_9 = []

for number in Chia9:
    if number % 9 == 0:
        divisible_by_9.append(number)

print("Danh sách các số chẵn từ 2020 đến 3838:")
print(Chia9)

print("Danh sách các số chẵn chia hết cho 9:")
print(divisible_by_9)
