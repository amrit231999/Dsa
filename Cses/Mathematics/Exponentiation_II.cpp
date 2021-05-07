#include <bits/stdc++.h>
#define int long long
using namespace std;
int mod = 1e9 + 7;
int modpow(int x, int n)
{
    int m = mod;
    if (n == 0)
        return 1 % m;
    long long u = modpow(x, n / 2);
    u = (u * u) % m;
    if (n % 2 == 1)
        u = (u * x) % m;
    return u;
}
signed main()
{

    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--)
    {
        int a, b, c;
        cin >> a >> b >> c;
        cout << (modpow(a, modpow(b, c))) << endl;
    }
    return 0;
}