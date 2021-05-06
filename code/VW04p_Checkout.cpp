#include <bits/stdc++.h>

using namespace std;

int main() {
    // Fast I/O
    ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

    double d, a1, a2, v, t;
    cin >> d >> a1 >> a2 >> v >> t;

    double a = double(1) / 2 / a1 + double(1) / 2 / a2;
    double delta = t * t + a * d * 4;

    double x = (-t + sqrt(delta)) / 2 / a;
    double result;
    if (x < v) {
        result = x / a1 + t + x / a2;
    } else {
        t = (d - v * v / 2 / a1 - v * v / 2 / a2) / v;
        result = v / a1 + t + v / a2;
    }

    cout << fixed << setprecision(12) << result << '\n';

    return 0;
}