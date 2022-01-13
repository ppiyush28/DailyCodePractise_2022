# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:39:33 2022

@author: Piyush
"""

# Minimum Absolute Difference

from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the original array 
        arr.sort()
        answer = []

        # Initialize minimum difference as a huge integer in order not 
        # to miss the absolute difference of the first pair. 
        min_pair_diff = float('inf')
        print("min_pair_diff:", min_pair_diff)
        
        # Traverse the sorted array and calcalute the minimum absolute difference.
        for i in range(len(arr) - 1):
            min_pair_diff = min(min_pair_diff, arr[i + 1] - arr[i])
        
        # Traverse the sorted array and check every pair again, if 
        # the absolute difference equals the minimum difference, 
        # add this pair to the answer list. 
        for i in range(len(arr) - 1):   
            if arr[i + 1] - arr[i] == min_pair_diff:
                print("min_pair_diff:", min_pair_diff)
                answer.append([arr[i], arr[i + 1]])
        
        return answer
    
s=Solution()

print(s.minimumAbsDifference([1,2,3,4]))