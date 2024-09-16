# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:31:53 2024

@author: Nguyen Thuy Thuy Linh
"""

Chan= []

for number in range(2020, 3839):
    if number % 2 == 0:
        Chan.append(number)

Chan_string = "\t".join(map(str, Chan))

print(Chan_string)
