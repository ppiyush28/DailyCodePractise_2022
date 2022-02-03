# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 00:09:40 2022

@author: Piyush
"""

#Palindrome Partitioning

#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

#A palindrome string is a string that reads the same backward as forward.



import collections


class palindrome(object):
    def __init__(self):
        self.memory = collections.defaultdict(list)
        
        
        
    def partition(self, s):
        if not s: return [[]]
        
        if s in self.memory: return self.memory[s]  # the memory trick can save some time
        print('self.memory',self.memory)
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        self.memory[s] = ans
        return ans
    
p = palindrome()

print(p.partition('aba'))