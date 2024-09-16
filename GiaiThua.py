# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:39:21 2024

@author: Nguyen Thuy Thuy Linh
"""
n = int(input("Nhập một số nguyên dương: "))

while n <= 0:
    print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    n = int(input("Nhập một số nguyên dương: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Giai thừa của {n} là {factorial}.")

