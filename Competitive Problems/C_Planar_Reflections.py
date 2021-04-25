import sys,math
input=sys.stdin.readline 
from collections import defaultdict
mod=(int)(1e9+7)
for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=1
    if k>1 :
        ans+=n
    i=k-2
    power=1
    temp=[i for i in range(1,n)]
    while i>0:
        cur=0
        for j in temp:
            ans+=j
            
        ans%=mod
        temp2=[]
        for j in range(n-1):
            temp2.append((cur+temp[len(temp)-1-j])%mod)
            cur+=temp[len(temp)-1-j]

        temp[:]=temp2
        i-=1

    print(ans)
