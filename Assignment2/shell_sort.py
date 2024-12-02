#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:06:22 2024

@author: bing
"""


"""
insertion_sort_with_gap(a_list, g) 
# a_list is a list of N numbers, and g is the gap
  for i from g to N-1
    v = a_list[i]
    j = i - g
    while j >= 0 and a_list[j] > v
       a_list[j+g] = a_list[j]
       j = j - g
    a_list[j+g] = v

shell_sort(a_list):
# G is a list of M gaps in the descending order
# in this assignment, we simply set G = [5, 3, 1]
  G = [a list of gaps]   
  for i from 0 to M-1
    insertion_sort_with_gap(a_list, G[i])

"""


def insertion_sort_with_gap(lst, g):
    length = len(lst)
    for i in range(g, length):
        v = lst[i]
        j = i - g
        while j >= 0 and lst[j] > v:
            lst[j + g] = lst[j]
            j -= g
        lst[j + g] = v
    # pass
        
def shell_sort(lst):
    G = [5, 3, 1]
    length = len(G)
    for i in range(length):
        insertion_sort_with_gap(lst, G[i])
    # pass



if __name__ == "__main__":
    
    lst = [ 10, 9, 5, 6, 8, 3, 2, 1, 4, 7]
    shell_sort(lst)
    print(lst)
    
    lst = [ 0, 1, 2, 3]
    shell_sort(lst)
    print(lst)
    


