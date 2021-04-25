for _ in range(int(input())):
    p,a,b,c=map(int,input().split())
    ans=min(a*((p+a-1)//a)-p,b*((p+b-1)//b)-p,c*((p+c-1)//c)-p)
    print(ans)