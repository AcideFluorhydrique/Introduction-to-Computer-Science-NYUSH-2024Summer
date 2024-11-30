#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:36:21 2024

@author: bing
"""
import math
def search_with_loop_limit(sorted_lst, n):
    
   ##input your code here
    k = 0
    F = False
    minimum = 0
    maximum = len(sorted_lst) - 1
    # while not F and k < int(math.log(len(sorted_lst),2)):
    while minimum <= maximum and k < 11:
        M = ((maximum + minimum) // 2 )
        if n == sorted_lst[M]:
            k += 1
            F = True
            return (F, k - 1)
        elif n > sorted_lst[M]:
            minimum = M + 1
            k += 1
        elif n < sorted_lst[M]:
            maximum = M -1
            k += 1
        
    return (F, k)
# integers = [1,77, 88, 99, 101, 203, 555, 896]
# print(search_with_loop_limit(integers, 896))


if __name__ == "__main__":
    
    
    integers = [77, 88, 99, 101, 203, 555, 896]
    print(search_with_loop_limit(integers, 101))
    print(search_with_loop_limit(integers, 1001))
    
    