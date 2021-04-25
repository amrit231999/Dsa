import sys
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
    q=int(input())
    d=defaultdict(list)
    for k in range(q):
        v=list(map(str,input().split()))
        if d[v[0]]:
            d[v[0]][int(v[1])]+=1
        else:
            d[v[0]]=[0,0]
            d[v[0]][int(v[1])]+=1
    ans=0
    # print(d)
    for i in d:
        ans+=max(d[i][0],d[i][1])

    print(ans)
            





