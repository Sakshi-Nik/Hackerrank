#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int n, q;
    cin >> n >> q;

    vector<vector<int>> v;

    // Input arrays
    for(int i = 0; i < n; i++) {
        int k;
        cin >> k;

        vector<int> temp;
        for(int j = 0; j < k; j++) {
            int x;
            cin >> x;
            temp.push_back(x);
        }

        v.push_back(temp);
    }

    
    for(int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << v[a][b] << endl;
    }

    return 0;
};

