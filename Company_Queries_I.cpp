#include<bits/stdc++.h>
using namespace std;
#define int long long
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
int up[200005][25];
vector<int> adj[200005];
int lev[200005];
int par[200005];
void dfs(int s, int p) {
    up[s][0]=p;
    for (auto i: adj[s]){
        if (i!=p) {
            lev[i] = lev[s] + 1;
            
            dfs(i,s);
        }
    }

}
int raise(int x, int y) {
    int z=0;
    int flag=0;
    if(x==1 && y>0){
        return -1;
    }
    while(y>0) {
        if(x<=0 ||z>20 || x>200001){
            flag=1;
            break;
        }
        if (y&1 && z<=20 ) x = up[x][z];
        z++; y>>=1;
    }
    if (flag) return -1;
    return x;
}
int lca(int x, int y) {
    if (lev[x] > lev[y]) swap(x,y);
    int d = lev[y] - lev[x];
    y = raise(y,d);
    if (x == y) return x;
    for (int i=20;i>=0;i--) {
        if (up[x][i] != up[y][i]) {
            x = up[x][i];
            y = up[y][i];
        }
    }
    return up[x][0];
}
signed main(){
    int n,q; 
    cin>>n>>q;
    for(int i=2;i<n+1;i++){
        int y; cin>>y;
        adj[i].push_back(y), adj[y].push_back(i);
        par[i]=y;
    }
    
    dfs(1,-1);
    for(int j=1;j<21;j++){
        for(int i=1;i<n+1;i+=1){
                    up[i][j] = up[up[i][j-1]][j-1];
        }
    }
  
    while(q--){
        int x,d; cin>>x>>d;
       cout<<raise(x,d)<<endl;
    }
    return 0;
}    


