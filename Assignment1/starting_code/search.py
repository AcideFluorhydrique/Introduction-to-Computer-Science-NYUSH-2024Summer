#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:45:30 2024

@author: bing
"""



def search(lst, n):
    loops = 0
    T = False
    ##input your code here
    while loops < len(lst):
        if n == lst[loops]:
            T = True
            loops += 1
            break
        else:
            loops += 1

    
    return (T, loops)
    


if __name__ == "__main__":
    
    integers = [99, 88, 77, 101, 203, 896, 555]
    print(search(integers, 101))
    print(search(integers, 1001))
    
    
        
        