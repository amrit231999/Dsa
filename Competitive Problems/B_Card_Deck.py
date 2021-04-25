from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    cnt=0
    j=n-1
    i=n-1
    cur_max=n
    temp=[]
    while cnt<n:
        while v[i]!=cur_max:
            temp.append(v[i])
            i-=1
        temp.append(v[i])
        temp.sort(reverse=True)
        flag=1
        # print (temp)
        for x in range(1,len(temp)):
                if temp[x-1]-temp[x]>1:
                    cur_max=temp[x-1]-1
                    flag=0
                    temp=temp[x:]
                    break
        if flag:
            cur_max=temp[len(temp)-1]-1
            temp=[]

        elif flag !=0 and len(temp)==1:
            cur_max-=1
            temp=[]
        # print (temp)
        for k in range(i,j+1):
            print(v[k],end=" ")
            cnt+=1
        j=i-1
        i-=1
        # print(temp,"curmax",cur_max)
    print("")
        