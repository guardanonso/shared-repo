#include <stdio.h>

int main(void){
    int q, divisore;
    q = 10;
    divisore = 3;

    q %= divisore;
    printf("%d", q);
}