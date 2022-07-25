# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:50:06 2022

@author: Welcome
"""

#K diff Pairs in an Array

count=0
class solution:
    def kdiffpair(self,arr,k):
        count=0
        for i in range(0,len(arr)):
            print('i >',i)
            for j in range(i+1,len(arr)):
                print('j>',j)
                if arr[i]-arr[j] == k or arr[j]-arr[i]==k:
                    count+=1
        print(count)
        return count
            
            
s = solution()

print(s.kdiffpair([1, 5, 3, 4, 2], 2))


#### --------------------------------------------- ####

#Is Subsequence 
# abc Is Subsequence ahbgdc

s = 'ahbgdc'

t='abc'
for p in s:
    print(p in s)
    
a=0
for p in range(0,len(s)):
    for t1 in range(1,len(t)):
        if s[p] == t[t1]:
            #a+=1
            print('true')
        else:
            print('false')
        #print('a',a)
        
        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
        if t == "":
            return False

        if len(s) == 1 and len(t) == 1:
            return s[0] == t[0]

        a = 0
        # idx=0
        b = 0
        for i in range(len(t)):
            # print(a,i)
            if a>=len(s):
                return True
            if s[a] == t[i]:

                a += 1

        # a += 1
        print(a)
        if a == len(s):
            return True
        else:
            return False
        
S=Solution()
s = 'ahbgdc'
t='abc'
print(S.isSubsequence(s, t))