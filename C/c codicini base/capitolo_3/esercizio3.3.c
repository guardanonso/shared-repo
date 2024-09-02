#include <stdio.h>
int main(void){
    // a
    int product;
    product *= 2;
    // b
    product = product * 2;
    // c
    unsigned int count;
    if (count > 10){
        puts("Count is greater than 10.");
    }
    // d
    int q = 10.0, divisore = 4.0;
    q %= divisore;
    printf("%d", q);
}