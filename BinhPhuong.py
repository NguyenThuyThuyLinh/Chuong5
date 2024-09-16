# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:54:34 2024

@author: Nguyen Thuy Thuy Linh
"""

import random

squares = []

num_values = 10

for _ in range(num_values):
     number = random.uniform(18, 99)
    
     square = number ** 2
    
     squares.append(square)


print("Danh sách các giá trị bình phương:")
for square in squares:
    print(f"{square:.2f}") 