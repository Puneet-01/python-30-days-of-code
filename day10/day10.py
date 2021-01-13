


if __name__ == '__main__':
    n = int(input())
a = []
while n>0 :
    a.append(n%2)
    n=int(n/2)
s=len(a)
c=0
max=c
for i in range(s):
    if a[i]==1 :
        c=c+1
        if c>max :
            max=c
    else :
        c=0
print(max)
            
