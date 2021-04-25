from collections import defaultdict
s=str(input())
d=defaultdict(int)
ans=0
left=0
for i in range(len(s)):
    if d[s[i]]>0:
        
        for j in range(left,d[s[i]]-1):
            if d[s[j]]<d[s[i]]:
                d[s[j]]=0
            
        ans=max(ans,i+1-d[s[i]])
        ans=max(ans,i-left)
        left=d[s[i]]
        d[s[i]]=i+1
        
        
    else:
        d[s[i]]=i+1
    print(d,ans)
        

j=len(s)-1
minx=1e9
maxx=-1
if j>=0:
    for x in d:
        if d[x]>0:
            minx=min(d[x],minx)
            maxx=max(d[x],maxx)
    ans=max(ans,maxx-minx+1)
if ans==0 and len(s)>0:
    print(len(s)) 
else :
    print(ans)