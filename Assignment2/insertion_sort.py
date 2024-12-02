#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:22:57 2024

@author: bing
"""




"""
Insertion sort is a sorting algorithm that is quite efficient for small or nearly sorted lists. 
Its idea is like the way we arrange cards when playing card games. Once we have a hand that is already sorted, 
and when we pick up a new card, we want to find the correct place to insert it to maintain the sorted order. 
So, we have to compare the rank of the new card with the ranks of the cards in our hands one by one and insert
it after the card whose rank is smaller than it. 

Now, we have a list of numbers and want to sort them using the insertion sort. 
You can imagine each number is a card. At the very beginning, you have the first number in your hand; 
then, you need to find the correct place for the 2nd number by comparing it with the 1st one. 
If it is greater than the 1st number, you should insert the 2nd number after it; otherwise, 
insert the number in front of it. And for the following numbers, the 3rd, 4th, 5th, and so on, you can sort them in the same way, i.e.,

   1. comparing the number with the sorted numbers;
   2. if there is a number that is smaller than it, inserting it after the number;
   3. otherwise, put the number at the beginning of the sorted number list.


You may refer to the following pseudocode,
"""
# insertion_sort(a_list) #a_list is a list of N numbers
#    for i from 1 to N-1
#       v = a_list[i]
#       j = i - 1
#       while j >= 0 and a_list[j] > v
#          a_list[j+1] = a_list[j]
#          decrement j by 1
#       a_list[j+1] = v 


def insertion_sort(lst):

   for i in range(1, len(lst)):
      v = lst[i]
      j = i - 1
      while j >= 0 and lst[j] > v:
         lst[j + 1] = lst[j]
         j -= 1
      lst[j + 1] = v
   # pass
if __name__ == "__main__":
    
    lst = [ 10, 9, 5, 6, 8, 3, 2, 1, 4, 7]
    insertion_sort(lst)
    print(lst)
    
    lst = [ 0, 1, 2, 3]
    insertion_sort(lst)
    print(lst)