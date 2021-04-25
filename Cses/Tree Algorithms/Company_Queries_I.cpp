#include<bits/stdc++.h>
using namespace std;
#define int long long
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
int up[21][200005];
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
        if (y&1) x = up[z][x];
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
        if (up[i][x] != up[i][y]) {
            x = up[i][x];
            y = up[i][y];
        }
    }
    return up[0][x];
}
void solve(){
    int n,q; 
    cin>>n>>q;
    for(int i=2;i<n+1;i++){
        int x; cin>>x;
        up[0][i] = x;
        adj[x].push_back(i), adj[i].push_back(x);
    }
    for(int i=0;i<21;i++){
        for(int j=1;j<n+1;j+=1){
            up[i][j] = up[i-1][up[i-1][j]];
        }
    }
    dfs(1,0);
    while(q--){
        int x,y; cin>>x>>y;
        cout<<lca(x,y)<<endl;
    }
}    