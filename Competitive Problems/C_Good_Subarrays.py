import sys
input=sys.stdin.readline 
from collections import defaultdict

for _ in range(int(input())):

    n=int(input())
    v=list(map(int,input().strip()))
    pref=[0 for i in range(len(v)+1)]
    d=defaultdict(int)
    d[0]+=1
    
    for i in range(1,n+1):
        pref[i]=v[i-1]+pref[i-1]
        d[pref[i]-i]+=1
  
    ans=0
    for key,val in d.items():
        if val>=2:
            ans+=(val*(val-1))//2
    print(ans)