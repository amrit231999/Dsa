import sys,math
input=sys.stdin.readline 

for _ in range(int(input())):
    n=int(input())
    X,Y=([],[])
    for i in range(2*n):
        x,y=map(int,input().split())
        if x==0:
            Y.append(abs(y))
        else:
            X.append(abs(x))

    X.sort(reverse=True)
    Y.sort(reverse=True)

    
    ans=0.0

    for i in range(n):
        ans+=math.sqrt(X[i]*X[i]+Y[i]*Y[i])
    
    print(ans)

