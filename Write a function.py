# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:26:59 2019

@author: Abhay Paliwal
"""

def is_leap(year):
    if year%4==0 and(year%100!=0 or year%400==0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))