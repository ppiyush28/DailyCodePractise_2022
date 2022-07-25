# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:42:06 2022

@author: Welcome
"""

1) Coding:
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:
Input: s = "abcd", k = 2
Output: "bacd"



2) Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"


s = "cbbd"
for i in range(0,len(s)):
    if s[:i]==s[:i][::-1]:
        for su in s[i:]:
            su.append(str(s[:i] + su))
print(su)
    
        
s = "cbbd"       
def longest_palin(s):
    n = len(s)
    if (n<2):
        return n
    start = 0
    max_l = 1
    for i in range(n):
        lw = i-1
        hi = i+1
        while (hi < n and s[hi]==s[i]):
            hi=hi+1
    
        while (lw >= 0 and s[lw]==s[i]):
            lw= lw+1
    
        while (lw >= 0 and hi < n and s[lw]==s[hi]):
            lw=lw-1
            hi=hi+1
        
        lenght = hi -lw - 1
    
        if (max_l < lenght):
            max_l = lenght
            start = lw +1
    print(s[start:start+max_l])
    return max_l
   
l = longest_palin(s)   
print(l)