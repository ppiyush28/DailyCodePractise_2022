# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:46:14 2022

@author: Welcome
"""

# nth magical number

# class solution:
#     def __init__(self):
#         None
        
#     def nmagical(self,n:int,a:int,b:int) -> int:
#         i = 1
#         nu = 2
#         while i <= n:
#             if (nu % a ==0 or nu % b ==0):
#                 if i==nu:
#                     ans=nu
#                     print('ans1',ans)
#                     return ans
#                     break
#                 else:
#                     i=i+1
#             else:
#                 nu=nu+1
#                 ans=nu
#                 print('ans2',ans)
#                 return ans
            


# s = solution()

# print(s.nmagical(4, 2, 5))


class solution:
    def nmagical(self,N,A,B):
        
        def gcb(a,b):
            while b:
                a,b=b,a%b
            return a
        
        def check(A,B,N,lcm,target):
            return target //A +target//B-target//lcm >= N
        
        
        lcm=A*B // gcb(A,B)
        left,right=min(A,B),max(A,B)*N
        while  left <= right:
            mid = left + (right -left) // 2
            if check(A,B,N,lcm,mid):
                right=mid-1
            else:
                left=mid+1
        return left % (10**9 + 7)
    
    
    # if def gcb, and check is written after main logic, it can`t call function and ended with below error
    #NameError: name 'gcb' is not defined


s = solution()

print(s.nmagical(4, 2, 5))

                
                
    