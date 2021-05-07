#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, m;
    cin >> n >> m;
    multiset<int> st;
    for (int i = 0; i < n; i += 1)
    {
        int x;
        cin >> x;
        st.insert(x);
    }
    for (int i = 0; i < m; i += 1)
    {
        auto it = st.rbegin();
        st.insert(*it / 2);
        auto low = st.lower_bound(*it);

        st.erase(low);
        }
    int ans = 0;
    for (auto i : st)
    {

        ans += i;
    }
    cout << ans;
}