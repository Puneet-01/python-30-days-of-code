#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    a=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        p=''
        y=emailID.find('@')
        p=emailID[y+1:]
        
        
        if p=='gmail.com':
            a.append(firstName)
    y=len(a)
    for i in range(y):
        for j in range(y-i-1):
            if a[j+1]<a[j]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                        
                        
    for i in range(len(a)):
        print(a[i])