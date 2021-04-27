#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
#define int long long int

int n, m, q;
vector<vector<pair<int, int>>> g;
vector<vector<int>> d;
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m >> q;
    g.resize(n + 1);
    d.assign(n + 1, vector<int>(n + 1, 1e18));

    for (auto i = 0; i < m; ++i)
    {
        int u, v, w;
        cin >> u >> v >> w;
        g[u].push_back({w, v});
        g[v].push_back({w, u});
        d[u][v] = min(d[u][v], w);
        d[v][u] = min(d[v][u], w);
    }
    for (int i = 1; i <= n; i++)
    {
        d[i][i] = 0;
    }

    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                d[i][j] = min(d[i][j],
                              d[i][k] + d[k][j]);
            }
        }
    }

    for (int i = 1; i <= q; i += 1)
    {
        int u, v;
        cin >> u >> v;
        if (d[u][v] != 1e18)
        {
            cout << d[u][v] << endl;
        }
        else
        {
            cout << -1 << endl;
        }
    }
}