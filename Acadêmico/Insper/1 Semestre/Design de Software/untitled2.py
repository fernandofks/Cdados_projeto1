#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:11:45 2019

@author: fernandokenjisakabe
"""
a=0
for i in range(1, 100):
    a=a+1/(2**(1/i))
print(a)

a = 5
b = 7
a=a+5
print(a)
print(b)

b-=3
c=a*b
c+=2
print(c)

def oi(c):
    print(c)
    return 0
    
b=oi(c)
print(oi(c))
