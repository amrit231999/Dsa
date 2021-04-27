#include <bits/stdc++.h>
#define int long long
using namespace std;

struct item
{
    int m, c;
};
struct segtree
{
    int size;
    vector<item> sums;
    void init(int n)
    {
        size = 1;
        while (size < n)
            size *= 2;
        sums.resize(2 * size);
    }

    item merge(item a, item b)
    {
        if (a.m < b.m)
            return a;
        if (a.m > b.m)
            return b;
        return {a.m, a.c + b.c};
    }

    void set(int i, int v, int x, int lx, int rx)
    {
        if (rx - lx == 1)
        {
            sums[x] = {v, 1};
            return;
        }
        int m = (lx + rx) / 2;
        if (i < m)
        {
            set(i, v, 2 * x + 1, lx, m);
        }
        else
        {
            set(i, v, 2 * x + 2, m, rx);
        }
        sums[x] = merge(sums[2 * x + 1], sums[2 * x + 2]);
    }
    void set(int i, int v)
    {
        set(i, v, 0, 0, size);
    }
    item sum(int l, int r, int x, int lx, int rx)
    {
        if (lx >= r || rx <= l)
            return {INT_MAX, 0};
        if (lx >= l && rx <= r)
            return sums[x];
        int m = (lx + rx) / 2;
        item s1 = sum(l, r, 2 * x + 1, lx, m);
        item s2 = sum(l, r, 2 * x + 2, m, rx);
        return merge(s1, s2);
    }
    item sum(int l, int r)
    {
        return sum(l, r, 0, 0, size);
    }
};
signed main()
{
    ios::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    segtree st;
    st.init(n);
    for (int i = 0; i < n; i++)
    {
        int v;
        cin >> v;
        st.set(i, v);
    }

    while (m--)
    {
        int op;
        cin >> op;
        if (op == 1)
        {
            int i, v;
            cin >> i >> v;
            st.set(i, v);
        }
        else
        {
            int l, r;
            cin >> l >> r;
            cout << st.sum(l, r).m << " " << st.sum(l, r).c << endl;
        }
    }
    return 0;
}