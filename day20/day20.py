#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count=0
for i in range(n-1):
    for j in range(i,n):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
            count=count+1
print("Array is sorted in",count,"swaps.")
print("First Element:",a[0],"\nLast Element:",a[n-1])
