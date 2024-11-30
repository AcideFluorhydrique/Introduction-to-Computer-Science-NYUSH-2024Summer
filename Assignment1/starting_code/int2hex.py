#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:09:16 2020

@author: xg7
"""

def int_to_hexa(int_code):
    ##modified the following to the tests


    result = ""

    # binary = bin(int_code)[2:]
    hexadecimal = "0123456789ABCDEF"
    
    if int_code == 0:
        return 0
        
    while int_code > 0:
        R = int_code % 16
        result = hexadecimal[R] + result
        int_code = int_code // 16
    return result




##---test of your code, don't change the followings---##
if __name__ == "__main__":
    int_code = 12
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)

    int_code = 16
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)

    int_code = 255
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)
