import sys,math
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
    n,w=map(int,input().split())
    ans=0
    v=list(map(int,input().split()))
    d=defaultdict(int)
    vis=[]
    for i in v:
        d[i]+=1
        if d[i]==1:
            vis.append(i)

    vis.sort(reverse=True)

    cnt=0
    while cnt<n:
        cur=0
        i=0
        while i<len(vis):
            if d[vis[i]]>0:
                if cur+vis[i]<=w:
                    cnt+=1
                    cur+=vis[i]
                    d[vis[i]]-=1
                    i-=1

            i+=1
                    

        ans+=1

    print(ans)

    