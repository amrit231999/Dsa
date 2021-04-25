import sys
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    v=list(map(str,input().strip()))
    ans=[1 for i in range(n)]
    c=0
    for i in range(1,n):
        if v[i]>v[i-1]:
            ans[i]=ans[i-1]+1
    print("Case #"+str(_+1)+": ",end="")
    print(*ans)

            





