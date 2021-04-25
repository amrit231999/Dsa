for _ in range(int(input())):
    n=int(input())
    r=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    s1,s2=(0,0)
    cur=0
    for i in range(n):
        s1=max(s1,cur+r[i])
        cur+=r[i]
    cur=0
    for i in range(m):
        s2=max(s2,cur+b[i])
        cur+=b[i]
    print(s1+s2)
    
    
