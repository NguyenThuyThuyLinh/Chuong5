# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:01:14 2024

@author: Nguyen Thuy Thuy Linh
"""
number = float(input("Nhập một số thực trong khoảng từ -89.9 đến 88.8: "))

while number < -89.9 or number > 88.8:
    print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    number = float(input("Nhập một số thực trong khoảng từ -89.9 đến 88.8: "))

print(f"Số bạn đã nhập là {number}, giá trị này hợp lệ.")
