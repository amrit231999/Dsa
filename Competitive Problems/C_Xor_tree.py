import sys
import threading
input=sys.stdin.readline 

def main():
    n=int(input())
    g=[[] for i in range(n+1)]
    par=[0 for i in range(n+1)]
    inv=[0 for i in range(n+1)]
    ans=[]

    def dfs(u):
        for v in g[u]:
            if v!=par[u]:
                par[v]=u
                dfs(v)

    def dfs2(u):
        
        if u==1 or par[u]==1:
            if cur[u-1]!=goal[u-1]:
                inv[u]+=1
                ans.append(u)
        else :
            inv[u]=inv[par[par[u]]]
            if inv[par[par[u]]]%2:
                cur[u-1]^=1
            if cur[u-1]!=goal[u-1]:
                inv[u]+=1
                ans.append(u)
        for v in g[u]:
            if v!=par[u]:
                dfs2(v)


    for i in range(n-1):
        u,v=map(int,input().split())
        g[u].append(v)
        g[v].append(u)

    dfs(1)

    cur=list(map(int,input().split()))
    goal=list(map(int,input().split()))

    dfs2(1)
    print(len(ans))
    for j in ans:
        print(j)
    
if __name__=="__main__":
    sys.setrecursionlimit(10**5+100)
    threading.stack_size(10**8)
    t = threading.Thread(target=main)
    t.start() 
    t.join() 