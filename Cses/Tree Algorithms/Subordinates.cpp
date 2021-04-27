#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
#define int long long int

int n, m;
int cc = 0;
vector<vector<int>> g;
vector<bool> vis;
vector<int> sub;

void dfs(int u)
{
    vis[u] = true;
    sub[u] = 1;
    for (auto v : g[u])
    {
        if (!vis[v])
        {
            dfs(v);
            sub[u] += sub[v];
        }
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    g.resize(n + 1);
    sub.resize(n + 1);
    vis.resize(n + 1);
    for (auto i = 2; i < n + 1; ++i)
    {
        int v;
        cin >> v;
        g[i].push_back(v);
        g[v].push_back(i);
    }
    for (int i = 1; i <= n; i += 1)
    {
        if (!vis[i])
        {
            dfs(i);
        }
    }

    for (int i = 1; i <= n; i += 1)
    {
        cout << sub[i] - 1 << " ";
    }
}