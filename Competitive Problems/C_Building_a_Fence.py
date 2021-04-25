for _ in range(int(input())):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    s=[0 for i in range(n)]
    s[0]=h[0]+k
    s[n-1]=h[n-1]+k
    for i in range(1,n-1):
        if h[i+1]>=h[i]:
            s[i]=h[i]+k-1+k
        else:
            s[i]=h[i]+k
    flag=0
    for i in range(1,n):
        if abs(s[i]-s[i-1])>=k:
            flag=1
    print(["YES","NO"][flag])