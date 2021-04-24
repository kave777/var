#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int msr = INT_MAX, kk = 0;
    sort(a.begin(), a.end());
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if ((a[i] + a[j] + a[k]) % 3 == 0) {
                    if (binary_search(a.begin(),a.end(),(a[i] + a[j] + a[k])/3)) {
                        kk++;
                        msr = min(msr, (a[i] + a[j] + a[k])/3);
                    }
                }
            }
        }
    }
    cout << kk << " " << msr;
}

