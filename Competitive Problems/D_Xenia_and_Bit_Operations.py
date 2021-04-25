import sys
input=sys.stdin.readline 

def buildTree(a):
    
    for i in range(n):
        tree[n + i] = a[i]
    c,par,cnt=(n,0,0)
    for i in range(n - 1, 0, -1):
        
        if par ==0:
            tree[i] = tree[2*i] | tree[2*i+1]
        else :
            tree[i] = tree[2*i] ^ tree[2*i+1]
        cnt+=1
        if cnt==c//2:
            c=c//2
            par^=1


def updateTree(index, value):

    tree[index + n] = value
    index+=n

    i = index
    par=0
    while i > 1: 
        i=i//2
        if par==0:
            tree[i] = tree[2*i] | tree[2*i+1]
        else :
            tree[i] = tree[2*i] ^ tree[2*i+1]
        par ^=1

n,m=map(int,input().split())
a=list(map(int,input().split()))

n=len(a)

tree=[0 for i in range(2*n+1)]
buildTree(a)

for _ in range(m):
    
    ind,val=map(int,input().split())
    if n==131072:
        #FOR DEBUG
        print(ind,val,tree[ind-1],tree[1])
    updateTree(ind-1,val)
    print(tree)
    print(tree[1])