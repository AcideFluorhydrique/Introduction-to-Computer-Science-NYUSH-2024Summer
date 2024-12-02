#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:40:42 2022

@author: bing
"""





"""
Write a function to generate binary strings of a given length n. 
The binary strings should not have consecutive 1s. 
You may design your algorithm by referring to the following figure. 
"""

def binary_string_without_consecutive_ones(n, binary_string=[], current_str=''):
    # pass
    def generate(n, current_str):
        if n == 0:
            binary_string.append(current_str)
            return
        generate(n - 1, current_str + "0")
        if not current_str or current_str[-1] != "1":
            generate(n - 1, current_str + "1")

    generate(n, "")
    return binary_string


    


    

if __name__=="__main__":
    n = 3
    binary_string = []
    print(binary_string_without_consecutive_ones(n, binary_string))
    n = 4
    binary_string = []
    print(binary_string_without_consecutive_ones(n, binary_string))
    