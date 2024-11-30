#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:50:19 2020

@author: xg7
"""

def convert_to_Roman_numeral(n):
    A = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    R = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    i = 0
    while n > 0:
        for j in range(n // A[i]):
            roman += R[i]
            n -= A[i]
        i += 1
    return roman
    # pass


##test
if __name__ == "__main__":
    n = 1800
    print(convert_to_Roman_numeral(n))


