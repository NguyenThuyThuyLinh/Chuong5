# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:47:58 2024

@author: Nguyen Thuy Thuy Linh
"""
import random

so_luong_phan_tu = random.randint(20, 30)

danh_sach = [random.randint(1, 100) for _ in range(so_luong_phan_tu)]

print(f"Số lượng phần tử trong danh sách: {so_luong_phan_tu}")
print("Danh sách các phần tử:", danh_sach)

