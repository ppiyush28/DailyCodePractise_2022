# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 21:29:05 2022

@author: Welcome
"""

#koko banana eating

class solution:
    def mineatingspeed(self,piles,h):
        
        def possible(speed):
            hour=0
            for pile in piles:
                hour +=pile/speed
                print('hour1',hour)
                #print('pile',piles[pile])
                if pile % speed !=0:
                    hour +=1
                    #print('hour2',hour)
            return hour <= h
        
        left,right =1,max(piles)
        while left < right:
            mid = left + (right-left)//2
            print('mid',mid)
            if possible(mid):
                right = mid
                print('right',right)
            else:
                left =mid + 1
                print('left',left)
        return left
    
s = solution()
    
print(s.mineatingspeed([30,11,23,4,20], 5))