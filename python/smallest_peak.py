# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:19:24 2022

@author: Welcome
"""
#kth smallesh element in sorted martix

from typing import List
from bisect import bisect

class smallestk:
    def ksmall(matrix:List[List[int]],k:int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            m = l + (r-l) // 2
            if sum(bisect.bisect(row,m) for row in matrix) < k:
                l = m+ 1
            else:
                r=m
        return l

s = smallestk()

print(s.ksmall(([0,2]),1))


#find peak element 
# peak element is > right and left element 

class Solution:
    def findpeakelement(self, arr : List[int]) -> int:
        n = len(arr)
        if n==1:
            return 0
        low = 0
        high = n -1
        while low <= high:
            mid = low + (high-low) //2
            print('mid', mid)
            
            if mid ==0:
                if arr[mid] > arr[mid+1]:
                    print('arr[mid]',arr[mid])
                    print('arr[mid+1]',arr[mid+1])
                    return mid
                else:
                    low= mid + 1
            elif mid == n - 1:
                if arr[mid] > arr[mid -1]:
                    print('arr[mid]',arr[mid])
                    print('arr[mid -1]',arr[mid-1])
                    return mid
                else:
                    high = mid -1
            else:
                if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                    print('arr[mid]',arr[mid])
                    print('arr[mid+1]',arr[mid+1])
                    print('arr[mid-1]',arr[mid-1])
                    return mid
                elif arr[mid] < arr[mid+1]:
                    print('arr[mid]',arr[mid])
                    print('arr[mid+1]',arr[mid+1])
                    low = mid+1
                else:
                    high = mid -1
                    
        return -1
                
p = Solution()

print(p.findpeakelement([3,6,4,1]))