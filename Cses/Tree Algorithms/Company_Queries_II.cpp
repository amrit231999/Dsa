#include<bits/stdc++.h>
using namespace std;
#define int long long
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
int up[200005][21];
vector<int> adj[200005];
int lev[200005];
void dfs(int s, int p) {
    for (auto i: adj[s]){
        if (i!=p) {
            lev[i] = lev[s] + 1;
            dfs(i,s);
        }
    }
}
int raise(int x, int y) {
    int z=0;
    while(y>0) {
        if (y&1) x = up[x][z];
        z++; y>>=1;
    }
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
        int x; cin>>x;
        up[i][0] = x;
        adj[x].push_back(i), adj[i].push_back(x);
    }
    
        for(int i=1;i<n+1;i+=1){
            for(int j=1;j<21;j++){
             up[i][j] = up[up[i][j-1]][j-1];
        }
    }
    dfs(1,0);
    while(q--){
        int x,y; cin>>x>>y;
        cout<<lca(x,y)<<endl;
    }
    return 0;
}    


