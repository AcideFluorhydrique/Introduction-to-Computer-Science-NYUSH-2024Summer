#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 12:17:19 2022

@author: bing
"""

def sum_a_list(lst):

    sum = 0
    for _ in lst:
        sum += _
    
    return sum


if __name__ == "__main__":
    
    sum_a_list([5, 4, 3, 2, 1])