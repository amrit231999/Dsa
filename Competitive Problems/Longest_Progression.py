import sys
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    d=defaultdict(list)
    diff=[]
    for i in range(1,n):
        diff.append(v[i]-v[i-1])

    if min(diff)==max(diff):
        print("Case #"+str(_+1)+":",n)
        continue
    cur=0
    i=0
    ans=-1
    while i<(len(diff)):
        k=i
        cur=0
        while k<len(diff) and diff[k]==diff[i] :
            k+=1
            cur+=1

        d[diff[i]].append([i,i+cur-1])
        
        if len(diff)-(i+cur-1)>=3 or i>=2:
            if i>=2:
                if diff[i-1]+diff[i-2]==2*diff[i]:
                    ans=max(ans,cur+3)

            if len(diff)-(i+cur-1)>=3 :
                 if diff[i+cur]+diff[i+cur+1]==2*diff[i]:
                    ans=max(ans,cur+3)
        ans=max(ans,cur+2)
        i=k

    for i in d:
        c=d[i]
        ans=max(ans,c[0][1]-c[0][0]+3)
        for j in range(1,len(c)):
            if c[j][0]-c[j-1][1]==3:
                if diff[c[j-1][1]+1]+diff[c[j-1][1]+2]==2*i:
                    ans=max(ans,c[j][1]-c[j-1][0]+2)

    print("Case #"+str(_+1)+":",ans)

    

    
            





