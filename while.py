# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:59:05 2024

@author: Nguyen Thuy Thuy Linh
"""
number = int(input("Nhập một số trong khoảng từ -99 đến 99: "))

while number < -99 or number > 99:
    print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    number = int(input("Nhập một số trong khoảng từ -99 đến 99: "))

print(f"Số bạn đã nhập là {number}, giá trị này hợp lệ.")