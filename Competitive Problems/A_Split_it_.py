import sys
input=sys.stdin.readline 
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=str(input())
    
    if k==0:
        print("YES")
        continue
    if n%2==0 and k==n//2:
        print("NO")
        continue
   
    s1=s[:(n+1)//2-1]
    s2=s[(n+1)//2:n]
    s3=s2[::-1]
    
    if n%2==0:
        s2=s[(n+1)//2+1:n]
        s3=s2[::-1]

    if s1==s3:
        print("YES")
    else :
        print("NO")