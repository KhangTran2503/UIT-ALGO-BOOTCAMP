#include <bits/stdc++.h>
using namespace std;

int main() {
    // Fast I/O
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) cin >> matrix[i][j];

    int result_sum = INT_MAX;
    for (int i = 0; i < n - 2; ++i)
        for (int j = 0; j < m - 2; ++j) {
            int current_sum = 0;

            for (int ix = 0; ix < 3; ++ix)
                for (int iy = 0; iy < 3; ++iy)
                    current_sum += matrix[i + ix][j + iy];

            result_sum = min(result_sum, current_sum);
        }

    cout << result_sum << '\n';

    return 0;
}