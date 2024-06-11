#include <stdio.h>

int main(void){
    int n;
    int sum;
    int a;
    
    printf("Test Data: ");
    scanf("%d", &n);

    for(a = 1; a<=n; a++){
        printf("%d ", a );
        sum = sum + a;
    }
    printf("\nThe sum of natural numbers up to %d terms is: %d", n, sum);
}