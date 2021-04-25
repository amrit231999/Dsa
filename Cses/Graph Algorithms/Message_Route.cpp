#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
#define int long long int

int n, m;
int cc=0;
vector<vector<int>> g;
vector<int> vis;
vector<int>par,d;

void bfs(int u,int p)
{
    queue<int>st;
    st.push(u);
    d[u]=0;
    while(st.size()>0){
        u=st.front();
        st.pop();
        vis[u]+=1;
        for(auto v:g[u]){
            if(!vis[v] && d[v]>d[u]+1){
                st.push(v);
                par[v]=u;
                d[v]=d[u]+1;
            }
        }
    }

}



int32_t main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	g.resize(n+1);
	vis.resize(n+1);
    d.assign(n+1,1e9);
    par.assign(n+1,-1);
	for(auto i = 0; i < m; ++i)
	{
		int u, v;
		cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u);
	}

	bfs(1,-1);
    if (!vis[n]){
        cout<<"IMPOSSIBLE";
    }
    else{
        
        vector<int>path;
        path.push_back(n);
        while(path.back()!=1){
            path.push_back(par[path.back()]);
        }
        cout<<path.size()<<endl;
        reverse(path.begin(),path.end());
        for (auto i:path){
            cout<<i<<" ";
        }




    }

	
}