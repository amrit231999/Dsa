for _ in range(int(input())):
    n=int(input())
    s=str(input())
    ans=[]
    cur=1
    prev='-1'
    for i in range(len(s)):
        if s[i]==prev:
            cur=cur^1
            ans.append(str(cur))
            
        else :
            ans.append('1')
            cur=1
        prev=ans[i]
            
    print(*ans)