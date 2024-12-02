#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:30:18 2024

@author: bing
"""

from math import sin, cos, pi
from matplotlib import pyplot as plt
import copy

def get_u_coordinates(s, t):
    
    '''it returns the coordinates (x, y)'''
    ux = (t[0] - s[0])/2 - (t[1] - s[1])*(3 ** 0.5)/2 + s[0]
    uy = (t[0] - s[0])*(3 ** 0.5)/2 + (t[1] - s[1])/2 + s[1]
    return (ux, uy)
    # pass

def get_s_coordinates(p1, p2):
    '''it returns the coordinates (x, y)'''
    sx = (2 * p1[0] + p2[0])/3
    sy = (2 * p1[1] + p2[1])/3
    return (sx, sy)
    # pass

def get_t_coordinates(p1, p2):
    '''it returns the coordinates (x, y)'''
    tx = (p1[0] + 2 * p2[0])/3
    ty = (p1[1] + 2 * p2[1])/3
    return (tx, ty)
    # pass


# def koch_curve(p1, p2, n, n_max):

#     """
#     We compute the coordinates recursively. For each segment in the Koch curve, 
#     we calculate the coordinates of the division points s, u, t, 
#     and return them in the order from p1 to p2, i.e., 
#     the return value is a list containing coordinates of p1, s, u, t, and p2;
#     the coordinates of a point is a tuple of (x, y). 
#     Please complete the function koch_curve in koch_curve.py.
#     """
#     # it returns a list of coordinates (x, y)
#     curve = [p1, p2]
#     while n < n_max:
#         curve_copy = copy.deepcopy(curve)
#         for i in range(len(curve_copy) - 1):
#             # line = [curve_copy[i], curve_copy[i + 1]]
#             s = get_s_coordinates(curve_copy[i], curve_copy[i+1])
#             t = get_t_coordinates(curve_copy[i], curve_copy[i+1])
#             u = get_u_coordinates(s,t)
#             curve.insert(i+1 , t)
#             curve.insert(i+1 , u)
#             curve.insert(i+1 , s)
#             # print(curve)
#             # curve = [curve[0], get_s_coordinates(curve[0], curve[1]), get_u_coordinates(get_s_coordinates(curve[0], curve[1]), get_t_coordinates(curve[0], curve[1]), get_t_coordinates(curve[0], curve[1]), curve[1]]
#         n += 1
#     return curve

def koch_curve(p1, p2, n, n_max):
    """
    We compute the coordinates recursively. For each segment in the Koch curve, 
    we calculate the coordinates of the division points s, u, t, 
    and return them in the order from p1 to p2, i.e., 
    the return value is a list containing coordinates of p1, s, u, t, and p2;
    the coordinates of a point is a tuple of (x, y). 
    Please complete the function koch_curve in koch_curve.py.
    """
    global C
    if n == 0:
        C = [p1]
    elif n == n_max:
        C.append(p2)
        return
    s = get_s_coordinates(p1, p2)
    t = get_t_coordinates(p1, p2)
    u = get_u_coordinates(s, t)
    koch_curve(p1, s, n + 1, n_max)
    koch_curve(s, u, n + 1, n_max)
    koch_curve(u, t, n + 1, n_max)
    koch_curve(t, p2, n + 1, n_max)
    return C

if __name__ == "__main__":
    p1 = (0, 0)
    p2 = (100, 0)
    n_max = 3
    coordinates = koch_curve(p1, p2, 0, n_max)
    
    ## Uncomment the following statements 
    ## They will plot the koch curve
    x = [c[0] for c in coordinates]
    y = [c[1] for c in coordinates]
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()
    
    