import sys
input=sys.stdin.readline 

n=int(input())
v=list(map(int,input().split()))
c=[i for i in range(n+1)]

for i in v:
    c[i]=0

c.sort()
cnt=c.count(0)
c=c[cnt:]

ind,rot=[],[]
j=0
for i in range(n):
    if v[i]==0:
        ind.append(i)
        v[i]=c[j]
        j+=1

# print(*v)
for i in range(n):
    if v[i]==i+1:
        rot.append(v[i])

if len(rot)==1:
    temp=rot[0]-1
    for i in ind :
        if v[i]!=rot[0]:
            k=i
            break
    swap=v[temp]
    v[temp]=v[k]
    v[k]=swap

elif len(rot)>1:
    rot2=[]
    for i in range (1,len(rot)):
        rot2.append(rot[i])

    rot2.append(rot[0])
    j=0
    for i in range(n):
        if v[i]==rot[j]:
            v[i]=rot2[j]
            j+=1
            if j==len(rot):
                break

print(*v)