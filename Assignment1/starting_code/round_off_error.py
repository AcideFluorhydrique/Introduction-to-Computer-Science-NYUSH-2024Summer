#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:48:42 2021

@author: bing
"""
def fraction2binary(f, space):
    ##complete the code
    b = ""
    # T = True
    while len(b) < space:
        f_times_two = f + f
        if f_times_two >= 1:
            b += "1"
            f = f_times_two - 1

        else:
            b += "0"
            f = f_times_two

    return "0."+ b


def binary2fraction(b):
    ##complete the code
    Integer, Decimal = b.split(".")
    i = -1
    output = 0
    for j in Decimal:
        output += int(j)*(2**i)
        i -= 1
    return output
    # pass
    

if __name__ =='__main__':
    print('2.07 - 2 =', 2.07 - 2)
    f = 0.07
    l = 52
    print('The binary of 0.07 in your machine:')
    print(fraction2binary(f, l))
    print('Influence of the Truncation error')
    print(binary2fraction(fraction2binary(f, l)))
    
