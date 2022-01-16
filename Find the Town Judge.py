# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 00:39:30 2022

@author: Piyush
"""

#Find the Town Judge

from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (N+1)
        print('Trusted',Trusted)
        print('[0]'),[0]
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
            
        for i in range(1, len(Trusted)):
            if Trusted[i] == N-1:
                return i
        return -1
    
    


    
s =Solution()

print(s.findJudge(2, [[1,2]]))