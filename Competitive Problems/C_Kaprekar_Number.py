n,k=map(int,input().split())
def func(n):
    g1=''.join(sorted(str(n),reverse=True))
    g2=''.join(sorted(str(n)))
    g1=int(g1)
    g2=int(g2)
    return g1-g2
sn=str(n)
sk=str(k)
a=[n for i in range(k+1)]
for i in range(1,k+1):
    a[i]=func(a[i-1])
print(a[k])