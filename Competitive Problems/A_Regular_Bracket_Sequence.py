for _ in range(int(input())):
    s=str(input())
    l=[]
    l[:]=s
    flag=0
    n=len(l)
    for i in range(len(l)):
        if l[i]=='(':
            indl=i
        if l[i]==')':
            indr=i
    if indr==0 or indl==n-1 or n%2:
        flag=1

    print(["YES","NO"][flag])

