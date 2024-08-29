#include <stdio.h>

int main(void){
    float galloni, miles, result;
    
    while(galloni != -1){
        printf("Enter the gallons used (-1 to end): ");
        scanf("%f", &galloni);
        printf("Enter the miles driven: ");
        scanf("%f", &miles);
        result = miles/galloni;
        printf("The miles/gallons is: %f\n", result);
    }
}