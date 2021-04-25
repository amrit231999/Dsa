import sys
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
    v=list(map(int,input().strip()))
    ans=1e10
    for i in range(len(v)):
        temp='0'
        for j in range(len(v)):
            if j!=i:
                temp+=str(v[j])

        # print(temp)

        cur=int(temp)
        ans=min(ans,cur)

    print(ans)

    
    
            





