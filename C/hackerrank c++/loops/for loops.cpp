#include <bits/stdc++.h>

using namespace std;
int main(void){
    int a, b, n;
    cin >> a;
    cin >> b;
    for(n=a; n<=b; n = n+1){
        int resto = n%2;
        if (n >=1 && n<=9){
            if(n == 1){
                cout<<"one\n";
            }
            else if(n == 2){
                cout<<"two\n";
            }
            else if(n == 3){
                cout<<"three\n";
            }
            else if(n == 4){
                cout<<"four\n";
            }
            else if(n == 5){
                cout<<"five\n";
            }
            else if(n == 6){
                cout<<"six\n";
            }
            else if(n == 7){
                cout<<"seven\n";
            }
            else if(n == 8){
                cout<<"eight\n";
            }
            else if(n == 9){
                cout<<"nine\n";
            }

        } 
        else if(n>9 && resto == 0){
            cout << "even\n";
        }
        else if(n>9 && resto!=0){
            cout << "odd\n";
        }

    }
}
