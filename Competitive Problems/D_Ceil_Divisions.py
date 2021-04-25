for _ in range(int(input())):
    n=int(input())
     
    if n<=8:
        temp=n
        cnt=0
        while temp!=1:
            temp=(temp+1)//2
            cnt+=1
        print(cnt+n-3)
        for i in range(3,n):
            print(i,n)
        for i in range(cnt):
            print(n,2)
    else:
        temp=n
        cnt=0
        while temp!=1:
            temp=(temp+7)//8
            cnt+=1
        print(cnt+n-1)
        for i in range(3,n):
            if i!=8:
                print(i,n)
        for i in range(cnt):
            print(n,8)
        
        print(8,2)
        print(8,2)
        print(8,2)
 
        