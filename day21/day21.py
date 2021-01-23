
import math
T=int(input())
for j in range(T):
        
    n=int(input())
    t=math.sqrt(n)
    t=int(t)

    b=1
   
    for i in range(2,t+1):
        if n%i==0:
            b=0
            break
    if b==1 and n!=1 and n!=0:
        print("Prime")
    else:
        print("Not prime")
