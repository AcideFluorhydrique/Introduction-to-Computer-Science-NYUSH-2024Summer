#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:08:56 2024

@author: bing
"""



def max_profit(prices):
    ##input your code here
    buy = prices[0]
    max_d = float('-inf')
    for i in range(1, len(prices)):
        
        d = prices[i] - buy
        
        if d > max_d:
            max_d = d
        
        if prices[i] < buy:
            buy = prices[i]
    
    return max_d 
    



if __name__ == "__main__":
    
    prices = [800, 300, 600, 200, 100]
    # print(max_profit(prices))
    print(max_profit(prices))

    prices = [800, 300, 200, 100, 0]
    # print(max_profit(prices))
    print(max_profit(prices))
        
        