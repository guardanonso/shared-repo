#include <stdio.h>
int main(void){ 
    int sum, x;
    sum = 0;
    x = 1;
    for(x ; x<= 10; x+=1){
        sum += x;
    }
    printf("The sum is: %d", sum);
}