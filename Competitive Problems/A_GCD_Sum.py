import sys,math
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
    n,w=map(int,input().split())
    ans=0
    for i in range(n,n+100000):
        temp=str(i)
        s=0
        for x in temp:
            s+=int(x)
        
        if math.gcd(i,s)>1:
            ans=i
            break

    print(ans)