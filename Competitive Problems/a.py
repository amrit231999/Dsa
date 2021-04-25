import sys
input=sys.stdin.readline 
from collections import defaultdict

for _ in range(int(input())):
    l,r,m=map(int,input().split())
    for i in range(l,r+1):

        if i-m%i<=r-l:
            c=r
            b=c-(i-m%i)
            a=i
            break

        elif m%i<=r-l:
            c=l
            b=l+m%i
            a=i
            break
    
    print(a,b,c)

