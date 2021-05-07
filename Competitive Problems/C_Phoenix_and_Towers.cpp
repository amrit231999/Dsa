#include <bits/stdc++.h>
#define int long long
using namespace std;
signed main()
{
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--)
    {
        int n, m, x;
        cin >> n >> m >> x;
        vector<int> v(n);
        for (int i = 0; i < n; i += 1)
        {
            cin >> v[i];
        }
        set<pair<int, int>> st;
        vector<int> v2 = v;
        map<int, vector<int>> mp;
        sort(v2.begin(), v2.end());
        for (int i = 0; i < m; i += 1)
        {
            st.insert({v2[i], i});
            mp[i].push_back(v2[i]);
        }
        sort(v2.rbegin(), v2.rend());
        for (int i = 0; i < n - m; i += 1)
        {
            auto it = st.begin();
            auto z = *it;
            mp[z.second].push_back(v2[i]);
            st.erase(*it);
            st.insert({z.first + v2[i], z.second});
        }

        map<int, vector<int>> mp2;
        for (auto it = mp.begin(); it != mp.end(); it++)
        {
            for (auto j : it->second)
            {
                mp2[j].push_back(it->first);
            }
        }
        cout << "YES" << endl;
        for (int i = 0; i < n; i++)
        {
            auto ans = mp2[v[i]][mp2[v[i]].size() - 1];
            cout << ans + 1 << " ";
            mp2[v[i]].pop_back();
        }
        cout << endl;
    }
    return 0;
}