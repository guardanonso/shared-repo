#include <stdio.h>
int main(void){
    unsigned int x, y;

    scanf("%u", &x);
    scanf("%u", &y);

    unsigned int i = 0;
    unsigned int power= 1;

    while(i<y){
        power *= x;
        i += 1;
    }
    printf("%u", power);
}