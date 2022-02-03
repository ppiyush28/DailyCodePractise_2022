# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 01:43:17 2022

@author: Piyush
"""

#Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)[2:]
        m=0
        for i in range(len(s)):
            if(s[i]=='0'):
                x=2**(len(s)-i-1)
                m+=x
        return m
    
    

s= Solution()

print(s.findComplement(3))

#011 > 100

