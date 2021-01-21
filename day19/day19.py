# Enter your code here. Read input from STDIN. Print output to STDOUT   
import sys
n=int(input())
phone_book=dict()
for i in range(n):
    s=input()
    a=s.split()
    phone_book[a[0]]=a[1]

query=sys.stdin.readline().strip()

while query:
    phno=phone_book.get(query)
    if phno:
        print(query+'='+phno)
    else:
        print("Not found")
    query=sys.stdin.readline().strip()

   