#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
#define int long long int

int n, m;
int cc = 0;
vector<vector<int>> g, comp;
vector<bool> vis;
vector<int> lead;

void dfs(int u)
{
	comp[cc].push_back(u);
	vis[u] = true;
	for (auto v : g[u])
	{
		if (!vis[v])
		{
			dfs(v);
		}
	}
}

int32_t main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	g.resize(n + 1);
	comp.resize(n + 1);
	vis.resize(n + 1);
	for (auto i = 0; i < m; ++i)
	{
		int u, v;
		cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u);
	}

	for (auto i = 1; i <= n; ++i)
	{
		if (!vis[i])
		{

			dfs(i);
			cc++;
		}
	}

	cout << cc - 1 << endl;
	if (cc > 1)
	{
		for (int i = 0; i < cc - 1; i += 1)
		{
			cout << comp[i][0] << " " << comp[i + 1][0] << endl;
		}
	}
}