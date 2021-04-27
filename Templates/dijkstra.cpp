#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
#define int long long int

int n, m;
vector<vector<pair<int, int>>> g;
vector<int> vis;
vector<int> par, d;

void dijkstra(int u, int p)
{
    set<pair<int, int>> st;
    st.insert({0, u});
    d[u] = 0;
    while (st.size() > 0)
    {
        auto cur = *st.begin();
        auto u = cur.second;
        st.erase(*st.begin());
        vis[u] += 1;
        if (d[u] < cur.first)
        {
            continue;
        }
        for (auto v : g[u])
        {
            if (!vis[v.second] && d[v.second] > d[u] + v.first)
            {
                d[v.second] = d[u] + v.first;
                st.insert({d[v.second], v.second});
                par[v.second] = u;
            }
        }
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    g.resize(n + 1);
    vis.assign(n + 1, 0);
    d.assign(n + 1, 1e18);
    par.assign(n + 1, -1);
    for (auto i = 0; i < m; ++i)
    {
        int u, v, w;
        cin >> u >> v >> w;
        g[u].push_back({w, v});
    }

    dijkstra(1, -1);
    if (!vis[n])
    {
        cout << "IMPOSSIBLE";
    }
    else
    {

        for (int i = 1; i <= n; i += 1)
        {
            cout << d[i] << " ";
        }
    }
}