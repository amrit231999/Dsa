import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
sys.setrecursionlimit(300000)
n,q=map(int,input().split())

tree=[[] for i in range(n+1)]
v=list(map(int,input().split()))
for i in range(len(v)):
    tree[2+i].append(v[i])
    tree[v[i]].append(2+i)
    
    
MAXN=n+1
up=[[0 for j in range(21)] for i in range(MAXN)]
 
def binary_lifting( src,  par):
    up[src][0] = par
    for i in range(1,21):
        if up[src][i-1] != -1:
            up[src][i] = up[up[src][i-1]][i-1]
        else :
            up[src][i] = -1
 
    for  child in tree[src]:
        if child != par :
            binary_lifting(child, src)
            
binary_lifting(1, -1)
# print(up)

            
for _ in range(q):
    v,k=map(int,input().split())
    k=bin(k).replace("0b", "")
    k=k[::-1]
    node=v
    for i in range(len(k)):
        if k[i]=='1':
            node=up[node][i]
    print(node)
            
    

    
    
    
            





