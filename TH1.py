# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:29:06 2024

@author: PC
"""
def xuli_chuoi(str_input):
  """Hàm xử lý chuỗi, thực hiện các yêu ký tự đặc biệt, chữ cái, số"""

  do_dai = len(str_input)
  print("Độ dài chuỗi:", do_dai)

   ky_tu_dac_biet = "!@#$%^&*()-+=./"

  dem_ky_tu_dac_biet = 0
  dem_chu_thuong = 0
  dem_chu_hoa = 0
  dem_so = 0

  for ky_tu in str_input:
    if ky_tu in ky_tu_dac_biet:
      dem_ky_tu_dac_biet += 1
    elif ky_tu.isalpha():
      if ky_tu.islower():
        dem_chu_thuong += 1
      else:
        dem_chu_hoa += 1
    elif ky_tu.isdigit():
      dem_so += 1

  print("Số lượng ký tự đặc biệt:", dem_ky_tu_dac_biet)
  print("Số lượng chữ cái thường:", dem_chu_thuong)
  print("Số lượng chữ cái hoa:", dem_chu_hoa)
  print("Số lượng chữ số:", dem_so)

str_input = input("Nhập chuỗi: ")

xuli_chuoi(str_input)
