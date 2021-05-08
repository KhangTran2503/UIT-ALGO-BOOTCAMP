#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<vector<int>> a;

// prefixsum2D[i][j] is sum of all elements in rectangle with top left conner (1,1) and bottom right conner (i,j)
vector<vector<ll>> prefixsum2D;

int n, m;


// get_sum(u1 ,v1 ,u2 ,v2 ) is sum of all elements in rectangle with top left conner (u1,v1) and bottom right conner (u2,v2)
ll get_sum(int u1,int v1,int u2,int v2){
    ll sum = prefixsum2D[u2][v2] - prefixsum2D[u2][v1 - 1] - prefixsum2D[u1 - 1][v2] + prefixsum2D[u1 - 1][v1 - 1];
    return sum;
}


int main(){
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n >> m;

    a.resize(n + 1,vector<int> (m + 1));
    prefixsum2D.assign(n + 1,vector<ll> (m + 1,0LL));

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++){
            cin >> a[i][j];

            // caculate prefixsum2D[i][j] 
            prefixsum2D[i][j] = prefixsum2D[i - 1][j] + prefixsum2D[i][j - 1] - prefixsum2D[i - 1][j - 1] + (ll)a[i][j];
        }

    
    int ans = INT_MAX;
    for (int i = 1; i <= n - 2; i++)
        for (int j = 1; j <= m - 2; j++){
                int u = i + 2;
                int v = j + 2;
                // caculate sum of all elements in rectangle with top left conner (i,j) and bottom right conner (u,v)
                ans = min(ans, (int)get_sum(i,j,u,v) );
        }

    cout << ans << '\n';


    return 0;
    
}

