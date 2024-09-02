#include <stdio.h>

int main(void){
    float gallons, miles, result;
    float gallons_sum = 0;
    float miles_sum = 0;

    while(1){
        printf("Enter the gallons used (-1 to end): ");
        scanf("%f", &gallons);

        if(gallons == -1){

            if (gallons_sum > 0){
                printf("The overall average miles/gallons was: %.2f", miles_sum/gallons_sum);   
                }
              
            else{
                printf("No gallons were entered, so I can't calculate the average miles/gallons.\n");
            }    
            break;
        }

        gallons_sum += gallons;

        printf("Enter the miles driven: ");
        scanf("%f", &miles);
        miles_sum += miles;

        result = miles/gallons;
        printf("The miles/gallons is: %f\n", result);

    }
}