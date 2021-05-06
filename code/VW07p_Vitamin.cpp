#include <bits/stdc++.h>

using namespace std;

int main() {
    // Fast I/O
    ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

    int n, x;
    cin >> n >> x;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> prefix_sum(n);
    partial_sum(a.begin(), a.end(), prefix_sum.begin());

    const int MAX = 1e9 + 7;
    vector<int> dp(x + 1, MAX);
    dp[0] = 0;

    for (int i = 0; i <= x; ++i)
        for (int j = 0; j < n; ++j)
            if (i >= prefix_sum[j]) {
                dp[i] = min(dp[i], dp[i - prefix_sum[j]] + j + 2);
            }

    int result = dp[x];
    for (int i = 0; i <= x; ++i)
        if (x - i >= prefix_sum[n - 1] &&
            (x - i - prefix_sum[n - 1]) % a[n - 1] == 0)
            result = min(
                result, dp[i] + n + 1 + (x - i - prefix_sum[n - 1]) / a[n - 1]);

    cout << (result == MAX ? -1 : result - 1) << '\n';

    return 0;
}