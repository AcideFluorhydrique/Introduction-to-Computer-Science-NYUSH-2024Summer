#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:12:38 2017

@author: xg7
"""

# Q1
def order(p, q, n):
    ##delete the following pass 
    ##and complete the function
    """
    Write a function order(p, q, n) that takes two multi-element tuples p and q, 
    and compares the element at index n, returns True if p[n] > q[n]. 
    Examples:
    >>> order((1, 2, 3), (2, 1, 4), 0)
    False
    >>> order((1, 2, 3), (2, 1, 4), 1)
    True
    >>> order((1, 2, 3), (2, 1, 4), 2)
    False
    """
    if p[n] > q[n]:
        return True
    else:
        return False
    # pass

# Q2
def first_max(order_f, l, n):
    ##delete the following pass 
    ##and complete the function
    """
    Use order to implement a function first_max(order_f, l, n). 
    l is a list of tuples; the function returns the first largest tuple in l. 
    The comparison of order is done using the order you implemented in B.1 (i.e., a tuple p is larger than q if p[n] > q[n]).

    Example: ('B', 6), ('X', 6) and ('P', 6) are all the largest on index 1, 
    but ('B', 6) is the correct result because it is the first largest:

    >>> tuplst = [('X', 5), ('B', 6), ('P', 4), ('X', 3), ('B', 5), ('P', 6)]
    >>> print(first_max(order, tuplst, 1)
    ('B', 6)
    """
    # max_number = float("-inf")

    select = l[0]
    for i in l:
        if order(i,select,n):
            select = i
    return select
    # pass


# Q3 
def last_max(order_f, l, n):
    ##delete the following pass 
    ##and complete the function
    select = l[-1]
    l_reverse = list(reversed(l))
    for i in l_reverse:
        if order(i,select,n):
            select = i
    return select    
    # pass


##testing part. 
##You code should pass the tests and give the correst outputs.
##You can comment out them temporarily if you want. 
if __name__ == "__main__":
    print("---testing---")
    result = order((1, 2, 3), (2, 1, 4), 0)
    print("order((1, 2, 3), (2, 1, 4), 0) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 1)
    print("order((1, 2, 3), (2, 1, 4), 1) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 2)
    print("order((1, 2, 3), (2, 1, 4), 2) returns:", result)
    t = [('X', 5), ('B', 6), ('P', 4), ('X', 3), ('B', 5),('P', 6)]
    print("t =", t)
    print("first_max(order, t, 1) returns:")
    print(first_max(order, t, 1))
    print("Bonus: last_max(order, t, 1) returns:")
    print(last_max(order, t, 1))
    