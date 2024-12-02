#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:15:18 2024

@author: bing
"""

def selection_sort(lst):
    """
    Selection sort is another simple sorting algorithm that sorts a list by repeatedly 
    finding the minimum element from the unsorted part of the list and moving it to the beginning 
    (Recall the figure in the slides of the Lecture). The pseudo-code is as follows,

    selection_sort(a_list) # a_list is a list of N numbers.
    for i from 0 to N-1
        min_j = i
        for j from i to N-1
            if a_list[j] < a_list[min_j]
                min_j = j
        swap a_list[i] and a_list[min_j]
    """

    for i in range(len(lst)):
        minimum_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minimum_index]:
                minimum_index = j
        lst[i], lst[minimum_index] = lst[minimum_index], lst[i]
    # pass

if __name__ == "__main__":
    
    lst = [ 10, 9, 5, 6, 8, 3, 2, 1, 4, 7]
    selection_sort(lst)
    print(lst)
    
    lst = [ 0, 1, 2, 3]
    selection_sort(lst)
    print(lst)