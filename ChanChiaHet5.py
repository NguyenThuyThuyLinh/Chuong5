# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:23:05 2024

@author: Nguyen Thuy Thuy Linh
"""
ChiaHetCho5 = []

for number in range(2018, 2829):
    # Kiểm tra nếu số là chẵn và chia hết cho 5
    if number % 2 == 0 and number % 5 == 0:
        ChiaHetCho5.append(number)

# In danh sách các số chẵn chia hết cho 5
print("Danh sách các số chẵn chia hết cho 5 từ 2018 đến 2828:")
print(ChiaHetCho5)
