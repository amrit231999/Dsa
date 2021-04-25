#include<bits/stdc++.h>
using namespace std;
#define int long long
int n;
vector<vector<int>>g;
vector<int>par,inv,cur,goal,ans;

void dfs(int u){
    
    for(auto v:g[u]){
        if (v!=par[u]){
            par[v]=u;
            dfs(v);
            
        }
    }

}
void dfs2(int u){
    if (u==1 or par[u]==1){
        if (cur[u-1]!=goal[u-1]){
            ans.push_back(u);
            inv[u]+=1;
        }
    }
    else{
        inv[u]=inv[par[par[u]]];
        if (inv[u]%2){
            cur[u-1]^=1;
        }
        if (cur[u-1]!=goal[u-1]){
            inv[u]+=1;
            ans.push_back(u);
        }

    }
    for(auto v:g[u]){
        if (v!=par[u]){
            dfs2(v);
        }
    }
}
signed main(){
    cin>>n;
    g.resize(n+1);
    inv.assign(n+1,0);
    par.assign(n+1,0);
    cur.assign(n+1,0);
    goal.assign(n+1,0);
    for (int i=0;i<n-1;i++){
        int u,v;
        cin>>u>>v;
        g[u].push_back(v);
        g[v].push_back(u);

    }


    dfs(1);

    for(int i=0;i<n;i++)cin>>cur[i];
    for(int i=0;i<n;i++)cin>>goal[i];

    dfs2(1);

    cout<<ans.size()<<"\n";
    for (auto i :ans){
        cout<<i<<"\n";
    }


    return 0;


}