# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:23:01 2023

@author: DC
"""

num=input("enter a number::")
num1=str(num)
if(len(num1)==12):
    print(num1)
else:
    if(len(num1)!=12):
        num2=12-len(num1)
        for i in range(0,num2):
            print("0",end="")
        print(num1)
