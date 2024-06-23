#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int n;
    int k;
    cin >> n ; 
    int arr[n];
    for(k = 0; k <n; k = k + 1){
        int digit;
        cin >> digit;
        arr[k] = digit;
    }
    for(k=k-1; k >=0; k = k-1){
        cout << arr[k] << " ";
    }
    
}

