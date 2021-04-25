import sys
input=sys.stdin.readline 
from collections import defaultdict
for _ in range(int(input())):
   n=int(input())
   v=list(map(int,input().split()))
   if n<=2:
       print(0)
       continue
   flag=1
   c_dec=-1e10
   c_inc=-1e10
   cnt_dec=0
   cnt_inc=0
   ind_dec=-1
   for i in range (n):
       if i==0:
           minm=v[i]+1
           continue
       elif v[i]>=v[i-1]:
           cnt_inc+=1
           c_temp=v[i]-v[i-1]
           if c_inc==-1e10:
                c_inc=c_temp
           elif c_temp!=c_inc:
                flag=0
       else:
            ind_dec=i-1
            cnt_dec+=1
            c_temp=v[i-1]-v[i]
            if c_dec==-1e10:
                c_dec=c_temp
            elif c_temp!=c_dec:
                flag=0

   if (flag==0):
        print(-1)
        continue
   c=c_inc
   if cnt_dec==0:
        print(0)
        continue

   elif cnt_dec>0:
        if cnt_inc==0:
            print(0)
            continue
        else:
            c=c_inc
            m_temp=v[ind_dec]+c-v[ind_dec+1]
            if m_temp>max(v):
                print(m_temp,c)
            else:
                print(-1)






