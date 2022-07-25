# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:41:18 2022

@author: Welcome
"""

#Binary Search

#linear search

target =-5
arr=[1,5,2]

for i in range(0,len(arr)):
    if arr[i]==target:
        print(i)
        break
    else:
        print(-1)
        
arr.sort()
low=arr[0]
high=arr[len(arr)-1]

mid = low+high/2
